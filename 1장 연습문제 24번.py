# 1장 연습문제 24번 

import heapq

num = [9,7,5,3,1]

n = len(num)

h = [] # 힙을 위한 리스트 
mylist= [] # 빈 리스트 
for i in range(n) :
    heapq.heappush(h,(num[i]))  # 힙에 num을 개별 요소로 저장

for i in range(n) :
    mylist.append(heapq.heapop(h)) # 힙 리스트를 반환 mylist 리스트에 저장

print("힙 리스트 출력",num)
print("mylsit 리스트 정렬되어 출력",mylist)