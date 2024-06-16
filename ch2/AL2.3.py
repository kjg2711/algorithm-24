# 알고리즘 B / 알고리즘 2.3
# 자연수의 제곱 계산 (O(n))

n = int(input("compute_square_B(n): "))

def compute_square_B(n) :    # n의 제곱 계산 함수. 알고리즘 B 사용
    sum = 0 
    for i in range(n) :     # i : 0, 1, ... n-1
        sum = sum + n       # 기본연산
    return sum 

print(compute_square_B(n))   # 함수를 호출하여 결과를 반환하고 그 결과를 출력

