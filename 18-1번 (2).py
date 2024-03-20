count = int(input("노드의 개수:"))
mylist = [] 
for i in range (count) :
    data = int(input("노드의 %d의 데이터:" %(i+1)) )
    mylist.append(data)

print("리스트의 내용:", mylist)