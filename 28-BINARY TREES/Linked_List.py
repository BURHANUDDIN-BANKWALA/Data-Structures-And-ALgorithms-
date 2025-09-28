class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

## PRINT LINKED LIST
def print_LL_rec(head):
    temp=head
    if temp==None:
        return
    
    print(temp.data)
    print_LL_rec(temp.next)

## TAKE INPUT
def take_input():
    value=int(input('Enter The Value Of Node-->'))
    head=None
    
    while(value!=-1):
        newNode=Node(value)
        if head==None:
            head=newNode
        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
        value=int(input('Enter The Value Of New Node-->'))
    
    return head

## LENGTH OF LINKED LIST TAIL RECURSION
def len_of_LL_rec(head,ans=0):
    temp=head
    if temp==None:
        return ans
    
    return len_of_LL_rec(temp.next,ans+1)

## INSERTION AT HEAD
def insertion_at_head(head,data):
    newNode=Node(data)
    newNode.next=head
    head=newNode
    return head

## INSERTION AT TAIL RECURSIVELY
def insertion_at_tail_rec(head,data):
    if head==None:
        newNode=Node(data)
        return newNode
    
    if head.next==None:
        newNode=Node(data)
        head.next=newNode
        return head
    
    head.next=insertion_at_tail_rec(head.next,data)
    return head

## INSERTION AT INDEX RECURSIVELY
def insertion_at_index_rec(head,data,index):
    ## BASE CASE
    if index==0:
        return insertion_at_head(head,data)
    
    if head==None:
        print('List Index Out Of Bounds')
        return head
    
    head.next=insertion_at_index_rec(head.next,data,index-1)
    return head

## DELET A NODE FROM HEAD
def del_node_head(head):
    newHead=head.next
    return newHead

## DELETE A NODE FROM TAIL RECURSIVELY
def del_a_node_tail_rec(head):
    ## BASE CASE
    if head==None or head.next==None:
        return None
    
    head.next=del_a_node_tail_rec(head.next)
    return head

## DELETE A NODE FROM INDEX RECURSIVELY
def del_a_node_index_rec(head,index):
    if head==None:
        print('List Index Out Of Bounds')
        return None
    if index==0:
        return head.next
    
    head.next=del_a_node_index_rec(head.next,index-1)
    return head

## DELETE A NODE BY VALUE RECURSIVELY
def del_node_by_value_rec(head,value):
    ## BASE CASE
    if head==None:
        print('NOT FOUND')
        return head
    if head.data==value:
        return head.next 
    
    
    
    if head.next.data==value:
        head.next=head.next.next
        return head.next
        
    head.next=del_node_by_value_rec(head.next,value)
    return head

## SEARCH IN LINKED LIST RECURSIVELY
def search_in_LL_rec(head,value,aux=0):
    if head==None:
        return 'Not Found'
    
    if head.data==value:
        return aux
    
    return search_in_LL_rec(head.next,value,aux+1)

## SEARCH WITH INDEX IN LINKED LIST RECURSIVELY
def search_with_index_rec(head,index):
    if head==None:
        return 'List Index Out Of Bounds'
    
    if index==0:
        return head.data
    
    return search_with_index_rec(head.next,index-1)

## MIDDLE OF THE LINKED LIST USING TWO POINTERS APPROACH
def middle_of_LL_two_pointers(head):
    if head==None:
        return None
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow.data  