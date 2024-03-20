mylist = []  # 빈 리스트

num = int(input("노드의 개수: "))  # 리스트의 크기

for i in range(num):
    data = int(input(f"노드 #{i + 1} 데이터: ")) # f 문자열 리터럴 
    mylist.append(data)  # 리스트에 저장

print("리스트의 내용:", mylist)  # 리스트에 저장된 데이터 출력1