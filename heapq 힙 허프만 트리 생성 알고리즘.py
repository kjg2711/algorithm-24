import heapq
def make_heap_tree(freq, label) :
    n = len(freq) # 문자의 개수 
    h = [] # 힙을 위한 리스트 

    for i in range(n) : #모든 문자를 최소합에 삽입
        heapq.heappush(h,(freq[i], label[i])) # (키,값) 삽입

    for i in range(1,n): # n-1번 병합 
        e1 = heapq.heappop(h)    # 가장 작은 트리
        e2 = heapq.heappop(h)    # 다음 작은 
        heapq.heappush(h, (e1[0]+e2[0], e1[1]+e2[1])) # 병합트리 삽입
        print(e1, "+", e2) #병합내용 출력

print(heapq.heappop(h))  # 최종 트리의 루트 출력
