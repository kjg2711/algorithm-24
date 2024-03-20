#10. List(리스트) - 리스트란, 리스트 사용 
a_list = [1,2,3] # 리스트는 대괄호로 작성 / ,콤마로 내부 원소를 구분  / 리스트 추가,삭제,수정 가능 
b_list = [] # 리스트를 선언 
print("a_list 출력: ",a_list) # a_list의 내부 원소를 출력 
print("a_list 0 인덱스 출력: ",a_list[0]) #a_list의 0 인덱스를 출력
# print("a_list 0 인덱스",a_list[4]) a_list의 4 인덱스 인덱스 범위를 벗어나면 에러 발생  

print("b_list 출력: ",b_list) # 빈리스트 출력
b_list.append(4) #b_list에 원소(4)를 추가 
print("b_list 출력: ",b_list) #원소가 추가된 b_list 출력 / b_list에 4가 추가됨 

my_list = a_list+b_list # 두 리스트를 +연산자로 합칠 수 있다.
print("my_list", my_list)

c_list = ["김종규, 김성규, 김법규"] # 리스트안에 문자열 
print("c_list 문자열 출력: ", c_list)

d_list= [5,6,7,8,9,] # 마지막 원소 뒤에 콤마를 남겨도 에러가 나지 않는다.
print("d_lsit 출력: ", d_list) 