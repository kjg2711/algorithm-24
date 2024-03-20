# 처음 큐에 F(0),F(1) 들어있고
# F(2) 계산할때 F(0)를 제거
# 새로 계산된 F(2)= F(0)+F(1) 다시 큐에 들어간다 

import collections
num1 = collections.deque()
num1.append(0)
num1.append(1)

print("F=(0) = 0")
print("F=(1) = 1")

for i in range(2, 10) : # 2부터 9까지 
    val1 = num1.popleft()
    val2 = num1.popleft()
    val3= val1 + val2 
    num1.appendleft(val2)
    num1.append(val3)
    print("F(%d) = "%i, val3)