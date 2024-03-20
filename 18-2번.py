#연결된 리스트를 출력하는 포로그램

class Node:
    def __init__ (self, elem, next=None):
        self.data = elem
        self.link = next

def printList(head, msg="생성된 연결 리스트:"):
    print(msg, end="")
    n = head
    while n != None :
        print(n.data, end="->")
        n = n.link
    print()

head = None
tail = None
count = int(input("노드의 개수: "))
for i in range(count):
    data = int(input("노드 #%d의 데이터"%(i+1)))
    n = Node(data, None)
    if head==None :
        head = tail = n 
    else :
        tail.link = n
        tail = n
printList(head)