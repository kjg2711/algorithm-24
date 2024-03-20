alist = []  # 빈 리스트
num2 = int(input("노드의 개수: "))  # 리스트의 크기

for i in range(num2):
    num1 = int(input("노드 #{} 데이터: ".format(i + 1)))  # f 문자열이 아닌 format 함수를 사용
    alist.append(num1)  # 리스트에 저장

print("리스트의 내용:", alist)  # 리스트에 저장된 데이터 출력