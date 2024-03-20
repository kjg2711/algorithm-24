# 24번 허프만코드 8.6절 책 360p
# 우선순위 큐를 이용해 숫자를 정렬하는 프로그램을 구현해보자

# 숫자로 이루어진 리스트를 입력받기 
# 우선순위 큐에 넣기
# 넣은 순서대로 하나씩 꺼내 
# 원래 리스트에 저장 

# heapq 모듈 사용 

import heapq

h= []


num1 = int(input("입력받을 숫자 갯수: "))

for _ in range(num1) :
    num2 = int(input("힙리스트에 저장할 숫자:"))
    heapq.heappush(h, num2)


print("힙 리스트에 저장된 숫자", h)

while h:
    print("반환된 숫자", heapq.heappop(h))

