# 알고리즘 2.6
# 이진수 변환에서 총 비트 수 계산 / 반복 알고리즘

n = int(input("양의 정수: "))

def binary_digits(n) :          # 입력 양의 정수 n
    count = 0                   # 이진수의 최소 길이는 0
    while n > 0 :               # n이 1보다 크면 더 나눌 수있음 
        count = count + 1       # count 증가
        n = n // 2              # // n의 몫을 구해 다시 n에 저장 (정수 나눗셈) 
                                # //는 결과가 int로 나타남 / /는 결과가 float로 나타남 
    return count                # count 반환

print("입력한 정수의 몫: ", binary_digits(n))

