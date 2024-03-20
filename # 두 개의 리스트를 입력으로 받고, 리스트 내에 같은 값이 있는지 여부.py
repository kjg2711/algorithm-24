def same_list(a_list, b_list):
    for s in a_list:   #a_listd의 모든 요소들이 s로 들어감
        if s in b_list:  #if문을 사용하여 b_list의 모든요소들을 s와 확인
            return True  # 있으면 Ture 반환
    return False # 없으면 False 반환

a_list = [1, 2, 3, 4, 5]
b_list = [4, 5, 6, 7, 8]

print(same_list(a_list, b_list))  # 출력: True