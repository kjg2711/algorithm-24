# 알고리즘 A / 알고리즘 2.2 
# 자연수의 제곱 계산 (O(1))

n = int(input("compute_square_A(n): "))

def compute_square_A(n) :       # n의 제곱 계산 함수. 알고리즘 A 사용
    return n*n                  # 기본연산 n*n

print(compute_square_A(n))      # 함수를 호출하여 결과를 반환하고 그 결과를 출력