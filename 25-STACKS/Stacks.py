import Linked_List as LL

class Stack:
    def __init__(self):
        self.__head=None
        self.__size=0
    
    def push(self,data):
        self.__size+=1
        newNode=LL.Node(data)

        if self.__head==None:
            self.__head=newNode
            return f'{data} Pushed In Stack'
        
        newNode.next=self.__head
        self.__head=newNode
        return f'{data} Pushed In Stack'
    
    def top(self):
        if self.__head==None or self.__size==0:
            return 'Empty Stack'
        
        return self.__head.data
    
    def pop(self):
        if self.__head==None or self.__size==0:
            return 'Empty Stack'
        
        data_at_top=self.__head.data
        self.__head=self.__head.next
        self.__size-=1
        return data_at_top
    
    def size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size==0