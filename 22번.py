import queue

instr = input("문자열 입력: ")
stack = queue.LifoQueue()

# 입력된 문자열을 스택에 역순으로 저장
for ch in instr:
    stack.put(ch)

# 스택에서 데이터를 꺼내어 출력
while not stack.empty():
    print(stack.get(), end='')

print()  # 개행
