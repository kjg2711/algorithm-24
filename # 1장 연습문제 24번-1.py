# 1장 연습문제 24번 
# 콤마로 숫자를 한번에 받아 리스트에 저장
import heapq

inputnum = input("숫자들을 입력하세요 (콤마로 구분): ") # 콤마로 구분된 숫자를 입력받음
num1 = [int(num) for num in inputnum.split(',')] # 입력받은 정수을 콤마 기준으로 나누어 여러 입력값을 저장 

n = len(num1) # 길이

h=[] # 힙을 위한 리스트 
mylist=[] # 빈 리스트

for i in range(n) :
    heapq.heappush(h,num1[i]) # num1을 heapqpush를 통해 h에 추가
print("h를 출력",h)

for f in range(n):
    mylist.append(heapq.heappop(h))  # heappop을 통해 h 반환 append를 통해 반환한 h를 mylsit로 추가 

# newlist = sorted(mylist, reverse=False) 
# print("mylsit를 출력",newlist ) 
