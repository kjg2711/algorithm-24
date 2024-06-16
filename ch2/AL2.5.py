# 알고리즘 2.5
# 리스트의 중복 항목 탐색

A = [1,2,3,4,5,6]       # 리스트 A : 같은 항목이 없는 리스트 
B = [1,1,2,2,3,3]       # 리스트 B : 같은 항목이 있는 리스트 

def unique_elements(A) :            # 리스트 A입력
    n = len(A)                      # 입력의 크기 = 리스트의 크기
    for i in range(n-1) :           # i : 0, 1, ... n-1
        for j in range(i+1, n) :    # j : i+1, i+2, ... n-1
            if A[i] == A[j] :       # 기본연산
                return False        # 같은 항목이 있으면 False 반환 
    return True                     # 같은 항목이 없으면 True 반환

print(A, unique_elements(A))
print(B, unique_elements(B))