# 24번 허프만코드 8.6절 책 360p
# 우선순위 큐를 이용해 숫자를 정렬하는 프로그램을 구현해보자

# 숫자로 이루어진 리스트를 입력받기 
# 우선순위 큐에 넣기
# 넣은 순서대로 하나씩 꺼내 
# 원래 리스트에 저장 

# heapq 모듈 사용 

import heapq

freq = [1,2,3,4,5,]
# n = len(freq) # 문자의 개수 
h = [] # 힙을 위한 리스트 

for f in freq : #모든 문자를 최소 힙에 삽입
        heapq.heappush(h, freq) # freq 리스트 전체가 추가 되는 경우로 리스트 전체가 단일 요소가 되어버림

e1 = heapq.heappop(h)    # 반환 
print("힙 리스트 출력", e1)

mylist = []

mylist.append(e1)
print("mylist 출력",e1)

##################################

import heapq

freq = [1, 2, 3, 4, 5]
h = []  # 힙을 위한 리스트
mylist = []  # 새로운 리스트를 만듭니다.

for f in freq:  # 모든 숫자를 최소 힙에 삽입합니다.
    heapq.heappush(h, f)  # 숫자를 힙에 삽입합니다.

while h:  # 힙이 비어있지 않은 동안
    e = heapq.heappop(h)  # 최소값을 힙에서 꺼내어
    mylist.append(e)  # mylist에 추가합니다.

print("mylist 출력", mylist) 


##################################
import heapq

freq = []  # 빈 리스트

for _ in range(3):
    num = int(input("숫자: "))
    freq.append(num)  # 사용자 입력을 freq 리스트에 추가합니다.

n = len(freq)
h = []  # 힙을 위한 리스트
mylist = []  # 결과 리스트

for i in range(n):
    heapq.heappush(h, freq[i])  # freq를 h에 순서대로 삽입합니다.

for _ in range(n):
    mylist.append(heapq.heappop(h))  # 힙에서 숫자를 꺼내어 mylist에 저장합니다.

print("freq:", freq)
print("mylist:", mylist)

##################################

import heapq

# 콤마로 구분된 숫자를 입력받음
input_str = input("숫자들을 입력하세요 (콤마로 구분): ")

# 입력받은 문자열을 콤마를 기준으로 나누어 숫자 리스트로 변환
freq = [int(num) for num in input_str.split(',')]

# 리스트를 최소 힙으로 변환
heapq.heapify(freq)

# 힙에서 숫자 하나씩 추출하여 출력
while freq:
    print(heapq.heappop(freq))