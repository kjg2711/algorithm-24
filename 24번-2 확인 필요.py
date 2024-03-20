import heapq

num = [5,3,1]
num1 = num(len)
h = []  # 힙을 위한 리스트
mylist = []  # 새로운 리스트를 만듭니다.

for i in num:  # 모든 숫자를 최소 힙에 삽입합니다.
    heapq.heappush(h, num1[i])  # 숫자를 힙에 삽입합니다.

print("힙 리스트 출력",h)

while h:  # 힙이 비어있지 않은 동안
    num = heapq.heappop(h)  # 최소값을 힙에서 꺼내어
    mylist.append(num1)  # mylist에 추가합니다.

print("mylist 출력", mylist) 
