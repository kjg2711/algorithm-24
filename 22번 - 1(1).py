mylist = []

# 문자열 입력 받아 리스트에 저장
str_input = input("문자열 입력: ")
mylist.append(str_input)

print("처음 저장된 문자열:", mylist)

# 저장된 문자열 삭제 및 출력
deleted_str = mylist.pop(-1)
print("삭제된 문자열:", deleted_str)

print("마지막 저장된 문자열:", mylist)

# 저장된 리스트 역순으로 출력
print("저장된 리스트 역순 출력:", mylist[::-1])
