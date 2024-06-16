# 알고리즘 2.7 
# 순환적인 팩토리얼 알고리즘 / 순환 알고리즘

n = int(input("팩토리얼 F(n) n 입력: "))

def factorial(n) :      # 순환적으로 구현한 factorial 함수
    if n == 1 :         # 종료 조건(초기조건)
        return 1        # 순환을 멈추는 부분 
    else:
        return n * factorial(n-1)   # 자기 자신을 순환적으로 호출 
     
print("F({}) = {}! : {}".format(n,n,factorial(n)))
print(factorial(n)) # 함수를 호출하여 결과를 반환하고 그 결과를 출력

