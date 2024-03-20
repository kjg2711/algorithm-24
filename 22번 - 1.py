mylist = [] 

#for i in range(1) :
str = input("문자열 입력:")
mylist.append(str)

print("처음 저장된 문자열", mylist)

#for _  in range(3) :    
print("삭제된 문자열",mylist.pop(-1))


print("마지막 저장된 문자열", mylist)