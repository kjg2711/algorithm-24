import heapq

# 빈 리스트 생성
freq = []

# 사용자로부터 1부터 5까지의 숫자 입력받기
for i in range(1, 6):
    num = int(input(f"숫자 {i} 입력: "))
    freq.append(num)

# 리스트를 최소 힙으로 변환
heapq.heapify(freq)

# 힙에서 숫자 하나씩 추출하여 출력
while freq:
    print(heapq.heappop(freq))
