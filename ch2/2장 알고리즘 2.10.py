# 알고리즘 2.10 
# 이진수 변환에서 총 비트 수 계산 / 순환 알고리즘 

n = int(input("양의 정수: "))
def binary_digits(n) :                  # 입력 양의 정수 n 
    if n <= 1 :                         # n이 1 이하이면 길이는 1 
        return 1                        
    else :                              # n이 1보다 크면 
        return 1 + binary_digits(n//2)  # 1 + n//2의 길이 
print(binary_digits(n))