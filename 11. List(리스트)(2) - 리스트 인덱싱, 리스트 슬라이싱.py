# 11. List(리스트)(2) - 리스트 인덱싱, 리스트 슬라이싱
str = " show how to index into sequences ".split() #split 함수를 통해 문자열을 구분가능하다.
print("a_list 출력: ", str) 

# list indexing(리스트 인덱싱)
print ("str[5] 출력 : ", str[5]) # 마지막열 str[5]
print ("str[-1]출력 : ", str[-1]) # 마지막열을 [-1]로 도 찾을 수 있다

# list slicing(리스트 슬라이싱) / 리스트변수[시작인덱스:종료인덱스:step]
print("str[1:4] :",str[1:4])
print("str[1:-1] : " ,str[1:-1]) # 음수 인덱싱도 가능 
print("str[3:] : ", str[3:])
print("str[:3] : ", str[:3])
print("str[:3] + str[3:] == str : ", str[:3] + str[3:] == str) # 같다면 True 출력
full_str = str[:]
print("str[:] 출력: ", full_str)

# step 
print("str[::2] step 출력: ",str[::2])
#step을 이용한 reverse
print("str[::-1] step reverse출력: ",str[::-1])

# 리스트를 복사하는 방법 두가지 
a_str = str.copy()
print("a_str 출력: ", a_str) # copy()함수

b_str = list(str)
print("b_str 출력: ", b_str) #list()함수