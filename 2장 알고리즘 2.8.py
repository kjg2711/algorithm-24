# 알고리즘 2.8 
# 반복구조의 팩토리얼 알고리즘 / 반복 알고리즘

n = int(input("팩토리얼 F(n) n 입력: "))

def factorial(n):              # 반복 구조로 구현함 Factorial 함수 
    result = 1
    for k in range(n, 0, -1):  # k: n, n-1, ..., 2, 1 
        result *= k            # 기본연산
    return result

print("F({}) = {}! : {}".format(n,n,factorial(n)))
print(factorial(n)) # 함수를 호출하여 결과를 반환하고 그 결과를 출력
