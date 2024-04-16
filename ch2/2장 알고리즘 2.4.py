# 알고리즘 C / 알고리즘 2.4
# 자연수의 제곱계산 (O(n^2))

n = int(input("compute_square_C(n): "))

def compute_square_C(n) :       # n의 제곱 계산 함수. 알고리즘 C 사용
    sum = 0 
    for i in range(n) :         # i : 0, 1, ... n-1
        for j in range(n) :     # i : 0, 1, ... n-1
            sum = sum + 1       # 기본연산 
    return sum 

print(compute_square_C(n))

