# 1장 연습문제 24번 
# 콤마로 숫자를 한번에 받아 리스트에 저장
import heapq

inputnum = input("숫자들을 입력하세요 (콤마로 구분): ") # 콤마로 구분된 숫자를 입력받음
num1 = [int(num) for num in inputnum.split(',')] # 입력받은 문자열을 콤마를 기준으로 나누어 숫자 리스트로 변환

freq = []

n = len(num1)
h=[] # 힙을 위한 리스트 
mylist=[] # 빈 리스트

for i in range(n) :
    heapq.heappush(h,num1[i]) # freq를 h에 삽입

for f in range(n):
    mylist.append(heapq.heappop(h))  # heappop을 통해 h가 mylist로 

print("힙 리스트 출력",num1)
print("mylsit 리스트 정렬되어 출력",mylist )
    
