import Linked_List as LL

class Queue:
    def __init__(self):
        self.__head=None
        self.__size=0
        self.__tail=None

    def size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size==0
    
    def enqueue(self,data):
        newNode=LL.Node(data)
        self.__size=self.__size+1

        if self.__head==None:
            self.__head=newNode
            self.__tail=newNode
        else:
            self.__tail.next=newNode
            self.__tail=newNode
        return f'{data} Enqueued'
    
    def front(self):
        if self.__head==None:
            print('Empty Queue')
            return None
        else:
            return self.__head.data
        
    def dequeue(self):
        if self.is_empty():
            print('Empty Queue')
            return int(0)
        
        self.__size-=1
        pop_data=self.__head.data
        self.__head=self.__head.next

        if self.__head==None:
            self.__tail==None
        
        return pop_data
        