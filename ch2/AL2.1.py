# 알고리즘 2.1 
# 순차 탐색 

A = [1, 2, 3, 4, 5]     # A는 리스트 
key = int(input("key: "))   # key는 탐색키  

def sequential_search(A, key):
    for i in range(len(A)): # i: 0, 1, ... len(A)n-1
        if A[i] == key:     # == 비교 연산자 
            return i        # 탐색 성공하면 인덱스 반환
    return -1               # 탐색에 실패하면 -1을 반환 

result = sequential_search(A, key)
print(result)       


