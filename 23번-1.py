import collections
num1 = collections.deque()
num1.append(0)
num1.append(1)


print("F=(0) = 0, F=(1) = 1")


count = int(input("F(n) n을 입력: "))

for i in range(count) : 
    val1 = num1.popleft()
    val2 = num1.popleft()
    val3= val1 + val2 
    num1.appendleft(val2)
    num1.append(val3)
    print("F(%d) = "%i, val3)