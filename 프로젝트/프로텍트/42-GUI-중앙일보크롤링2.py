import sys
import urllib.parse as par
import urllib.request as req
from collections import Counter
import os

import pandas as pd
import matplotlib.pyplot as plt
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QThread, QObject, QDate
from PySide6.QtCore import Signal as pyqtSignal
from PySide6.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from wordcloud import WordCloud
from ui_crawling import Ui_Dialog
from ui_Sentiment_ui import Ui_MainWindow  # Import the sentiment UI

# JAVA_HOME 설정 확인
print("JAVA_HOME:", os.environ.get('JAVA_HOME'))

CalUI = "./crawling.ui"

class Worker(QObject):
    crawling_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(bool)
    wordcloud_progress_signal = pyqtSignal(str)
    finish_wordcloud_signal = pyqtSignal(WordCloud)

    def __init__(self):
        super().__init__()
        self.option_excel = False
        self.filename = ""
        self.option_date = False
        self.start_date = ""
        self.end_date = ""
        self.option_num = False
        self.max_crawling_num = -1
        self.option_wordcloud = False

    def write_excel(self, df):
        # 지정된 경로로 파일 저장
        save_dir = "./result/엑셀파일"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, f"{self.filename}.xlsx")

        writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name="Sheet1", index=None)
        worksheet = writer.sheets["Sheet1"]
        for idx, col in enumerate(df):
            series = df[col]
            max_len = max(series.astype(str).map(len).max(), len(col)) + 1
            worksheet.set_column(idx, idx, max_len)
        writer.close()

    def make_wordcloud(self, output):
        try:
            self.wordcloud_progress_signal.emit("형태소 분석 중입니다...")
            spliter = Okt()
            nouns = spliter.nouns(output)
            count = Counter(nouns)
            count = {i: count[i] for i in count if len(i) > 1}
            self.wordcloud_progress_signal.emit("단어 구름 만드는 중입니다...")
            font_path = "C:/Windows/Fonts/NanumGothic.ttf"  # 적절한 폰트 파일 경로로 변경
            wordcloud = WordCloud(font_path=font_path, background_color='white', width=400, height=400).generate_from_frequencies(count)
            self.finish_wordcloud_signal.emit(wordcloud)
        except Exception as e:
            print(f"Error during wordcloud generation: {e}")
            self.wordcloud_progress_signal.emit("단어 구름 생성에 실패했습니다.")

    def crawling(self, received_keyword):
        try:
            max_crawling_num = self.max_crawling_num if self.option_num else -1
            encoded = par.quote(received_keyword)
            page_num = 1

            df = pd.DataFrame(columns=["제목", "링크", "날짜/시간", "본문 내용"])
            current_crawling_num = 0
            output_total = ""

            while True:
                if self.option_date:
                    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&startDate={self.start_date}&endDate={self.end_date}&sfield=all&sort=&pageItemId=439&page={page_num}"
                else:
                    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&sort=&pageItemId=439&page={page_num}"

                code = req.urlopen(url)
                soup = BeautifulSoup(code, "html.parser")
                title = soup.select("ul.story_list h2.headline a")
                date = soup.select("li p.date")
                if not title:
                    break

                for i in range(len(title)):
                    try:
                        code_news = req.urlopen(title[i].attrs["href"])
                        soup_news = BeautifulSoup(code_news, "html.parser")
                        content = soup_news.select_one("div#article_body")
                        content_result = content.text.strip().replace("     ", " ").replace("   ", "")
                        if self.option_wordcloud:
                            output_total += content_result
                        result = f"""제목 : {title[i].text}
링크 : {title[i].attrs["href"]}
날짜/시간 : {date[i].string}
{content_result}\n"""

                        self.crawling_signal.emit(result)

                        if self.option_excel:
                            df = pd.concat([df, pd.DataFrame([[title[i].text, title[i].attrs["href"], date[i].string, content_result]], columns=["제목", "링크", "날짜/시간", "본문 내용"])], ignore_index=True)
                        current_crawling_num += 1
                        if current_crawling_num == max_crawling_num:
                            break
                    except Exception as e:
                        print(f"Error processing article: {e}")
                        continue

                else:
                    page_num += 1
                    continue
                break

            if self.option_excel:
                self.write_excel(df)
            if self.option_wordcloud:
                self.make_wordcloud(output_total)
            self.progress_signal.emit(True)

        except Exception as e:
            print(f"Error during crawling: {e}")
            self.progress_signal.emit(False)

class SentimentDialog(QMainWindow):
    def __init__(self, filename):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = filename
        self.load_news_titles()
        self.ui.pushButton.clicked.connect(self.analyze_sentiment)
        self.ui.pushButton_2.clicked.connect(self.close)

    def load_news_titles(self):
        self.df = pd.read_excel(self.filename)
        self.ui.listWidget.addItems(self.df['제목'].tolist())
        self.ui.listWidget.currentItemChanged.connect(self.display_article)

    def display_article(self, current, previous):
        if current:
            index = self.ui.listWidget.row(current)
            article = self.df.iloc[index]['본문 내용']
            self.ui.textBrowser.setText(article)

    def analyze_sentiment(self):
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            index = self.ui.listWidget.row(current_item)
            article = self.df.iloc[index]['본문 내용']
            # 감성 분석 로직을 여기에 추가
            sentiment_score = self.perform_sentiment_analysis(article)
            if sentiment_score > 0:
                sentiment = "긍정적"
            else:
                sentiment = "부정적"
            self.ui.label_2.setText(f"{abs(sentiment_score)}% [{sentiment}]인 감정으로 분석되었습니다.")

    def perform_sentiment_analysis(self, text):
        # 감성 분석 알고리즘 구현
        # 간단한 예로, 단어 수 기반으로 감성 분석 점수를 계산
        positive_words = ['좋다', '행복하다', '사랑한다']
        negative_words = ['나쁘다', '슬프다', '미워하다']
        score = 0
        for word in positive_words:
            score += text.count(word)
        for word in negative_words:
            score -= text.count(word)
        return score

class MainDialog(QDialog, Ui_Dialog):
    start_signal = pyqtSignal(str)
    send_valve_popup_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("뉴스 크롤러")
        self.resize(1600, 1080)  # 윈도우 크기 조정
        self.label_start_date.setText(self.start_date.selectedDate().toString("yyyy-MM-dd"))
        self.label_end_date.setText(self.end_date.selectedDate().toString("yyyy-MM-dd"))
        self.group_excel.setEnabled(False)
        self.group_num.setEnabled(False)
        self.group_date.setEnabled(False)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.layout_wordcloud.addWidget(self.canvas)

        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        self.pushButton.clicked.connect(self.crawling_start)
        self.worker.crawling_signal.connect(self.show_result)
        self.start_signal.connect(self.worker.crawling)
        self.option_excel.stateChanged.connect(self.option_excel_check)
        self.option_date.stateChanged.connect(self.option_date_check)
        self.option_num.stateChanged.connect(self.option_num_check)
        self.option_wordcloud.stateChanged.connect(self.option_wordcloud_check)
        self.slider_num.valueChanged.connect(self.setting_num_in_line_edit)
        self.worker.progress_signal.connect(self.finish_crawling)
        self.send_valve_popup_signal.connect(self.all_clear_window)
        self.start_date.clicked[QDate].connect(self.show_start_date)
        self.end_date.clicked[QDate].connect(self.show_end_date)
        self.worker.wordcloud_progress_signal.connect(self.wordcloud_status.setText)
        self.worker.finish_wordcloud_signal.connect(self.show_wordcloud)

        self.pushButton_2.clicked.connect(self.open_sentiment_analysis)  # 버튼 연결

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)

    def show_wordcloud(self, wordcloud):
        self.fig.clear()  # 추가: 이전 그림을 지우기 위해
        ax = self.fig.add_subplot(111)
        self.fig.tight_layout()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis('off')
        self.canvas.draw()
        self.wordcloud_status.setText("단어 구름 생성 완료!")

    def show_start_date(self, date):
        self.label_start_date.setText(self.start_date.selectedDate().toString("yyyy.MM.dd"))

    def show_end_date(self, date):
        self.label_end_date.setText(self.end_date.selectedDate().toString("yyyy.MM.dd"))

    def all_clear_window(self):
        self.lineEdit_keyword.clear()
        self.textBrowser.clear()
        self.pushButton.setEnabled(True)

    def finish_crawling(self, is_finished):
        if is_finished:
            msg = QMessageBox()
            msg.setWindowTitle("안내")
            msg.setText("크롤링이 완료되었습니다.")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = msg.exec()
            if result == QMessageBox.Yes:
                self.open_sentiment_analysis()

    def open_sentiment_analysis(self):
        if self.worker.option_excel and self.worker.filename:
            self.sentiment_dialog = SentimentDialog(f"./result/엑셀파일/{self.worker.filename}.xlsx")
            self.sentiment_dialog.show()

    def setting_num_in_line_edit(self, value):
        self.lineEdit_num.setText(str(value))

    def option_num_check(self, state):
        self.group_num.setEnabled(state)
        self.worker.option_num = bool(state)

    def option_wordcloud_check(self, state):
        self.worker.option_wordcloud = bool(state)

    def option_date_check(self, state):
        self.group_date.setEnabled(state)
        self.worker.option_date = bool(state)

    def option_excel_check(self, state):
        self.group_excel.setEnabled(state)
        self.worker.option_excel = bool(state)

    def crawling_start(self):
        self.pushButton.setEnabled(False)
        keyword = self.lineEdit_keyword.text()
        if self.option_excel.isChecked():
            self.worker.filename = self.filename.text()
        if self.option_date.isChecked():
            self.worker.start_date = self.start_date.selectedDate().toString("yyyy-MM-dd")
            self.worker.end_date = self.end_date.selectedDate().toString("yyyy-MM-dd")
        if self.option_num.isChecked():
            self.worker.max_crawling_num = int(self.lineEdit_num.text())

        self.start_signal.emit(keyword)

    def show_result(self, result):
        self.textBrowser.append(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec())


