import sys
import os
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtCore import Qt, QAbstractTableModel
from ui_search import Ui_Form
import requests
from bs4 import BeautifulSoup

# 기사 크롤링 함수
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # <p> 태그와 data-divno 속성을 가진 요소들을 찾습니다.
        article_body = soup.find_all('p', {'data-divno': True})
        
        if article_body:
            # 모든 <p> 태그의 내용을 합칩니다.
            content = " ".join([p.text.strip() for p in article_body])
        else:
            content = "Content not found"
        return content
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return "Error fetching the URL"
    except Exception as e:
        print(f"Error parsing the article: {e}")
        return "Error parsing the article"

# 호스플 매칭 알고리즘
def horspool_string_matching(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)
    matches = []

    if pattern_length > text_length:
        return matches

    bad_character = {pattern[i]: pattern_length - i - 1 for i in range(pattern_length - 1)}

    i = pattern_length - 1
    while i < text_length:
        j = pattern_length - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j < 0:
            matches.append(k + 1)
            i += pattern_length
        else:
            i += bad_character.get(text[i], pattern_length)
    
    return matches

def simple_hash_function(word):
    return sum(ord(char) for char in word)

def index_sentences(sentences, target_word):
    index = []
    for i, sentence in enumerate(sentences):
        if target_word in sentence:
            index.append(i + 1)  # 인덱스를 1부터 시작하도록 수정
    return index

def count_word_occurrences(sentences, target_word):
    count = 0
    for sentence in sentences:
        count += sentence.count(target_word)
    return count

def search_word_in_article(url, target_word):
    article_content = scrape_article(url)
    sentences = article_content.split('.')
    
    string_matching_results = []
    for i, sentence in enumerate(sentences):
        matches = horspool_string_matching(sentence, target_word)
        if matches:
            string_matching_results.append((i + 1, [match - 1 for match in matches]))  # 위치에서 1을 빼서 출력
    
    hash_value = simple_hash_function(target_word)
    word_index = index_sentences(sentences, target_word)
    word_count = count_word_occurrences(sentences, target_word)
    
    return string_matching_results, hash_value, word_index, word_count, article_content

class ExcelTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value) if pd.notna(value) else ""
        return None

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Excel Search Application")

        self.ui.pushButton.setEnabled(False)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.load_excel_files()
        self.ui.listWidget.currentItemChanged.connect(self.on_file_selected)
        self.ui.pushButton.clicked.connect(self.on_search_clicked)

        self.selected_file = None
        self.search_results = None

    def load_excel_files(self):
        result_dir = "./result"
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        for root, dirs, files in os.walk(result_dir):
            for filename in files:
                if filename.endswith(".xlsx"):
                    full_path = os.path.join(root, filename)
                    self.ui.listWidget.addItem(full_path)

    def on_file_selected(self):
        self.selected_file = self.ui.listWidget.currentItem().text()
        self.ui.pushButton.setEnabled(True)

    def on_search_clicked(self):
        keyword = self.ui.lineEdit.text()
        if self.selected_file and keyword:
            df = pd.read_excel(self.selected_file)

            # 기사 본문 내용을 파싱하여 검색
            results = []
            for index, row in df.iterrows():
                url = row['링크']
                title = row['제목']
                try:
                    string_matching_results, hash_value, word_index, word_count, article_content = search_word_in_article(url, keyword)
                    if word_count > 0:
                        results.append({
                            '제목': title,
                            '링크': url,
                            '단어 해시값': hash_value,
                            '단어 위치': word_index,
                            '단어 횟수': word_count,
                            '본문 내용': article_content
                        })
                except Exception as e:
                    print(f"Error processing article: {e}")
                    continue

            search_results = pd.DataFrame(results)
            self.search_results = search_results
            self.update_table_view(search_results)

    def update_table_view(self, data):
        model = ExcelTableModel(data)
        self.ui.tableView.setModel(model)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.on_table_selection_changed)
        self.ui.tableView.resizeColumnsToContents()  # 컬럼 크기 자동 조정

        # 컬럼 너비가 충분하지 않을 경우 수동으로 조정
        for column in range(model.columnCount(None)):
            self.ui.tableView.setColumnWidth(column, 300)

    def on_table_selection_changed(self):
        selected_row = self.ui.tableView.currentIndex().row()
        if self.search_results is not None and selected_row >= 0:
            article_title = self.search_results.iloc[selected_row]["제목"]
            article_content = self.search_results.iloc[selected_row]["본문 내용"]
            self.ui.label.setText(article_title)
            self.ui.textBrowser.setText(article_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.resize(1600, 850)  # 창 크기 조정
    window.show()
    sys.exit(app.exec())

