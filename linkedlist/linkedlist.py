class LinkedList:
    
    class Node:
        def __init__(self,  data=0):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        return;
    
    def push(self,  data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode;
    
    def length(self):
        len = 0
        current = self.head
        while current is not None:
            len += 1
            current = current.next
        return len
    
    #1
    def count(self,  data):
        count = 0
        current = self.head
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next
        return count
    
    #2
    def getNth(self,  index):
        current = self.head
        i = index
        while current is not None:
            if i == 0:
                return current.data
            i -= 1
            current = current.next
        return -1
    
    #3
    def deleteList(self):
        current = self.head
        while current is not None:
            deleteMe = current
            current = current.next
            #the point of the assignment is to free memory, so that would happen here if this weren't in python
            del deleteMe.data
            deleteMe.next = None
        self.head = None
    
    #4
    def pop(self):
        deleteMe = self.head
        if deleteMe is None:
            raise Exception("list is empty - can't pop()")
        self.head = deleteMe.next
        data = deleteMe.data
        del deleteMe.data
        deleteMe.next = None
        return data
    
    #5
    def insertNth(self,  index,  data):
        if index == 0:
            self.push(data)
            return
        
        current = self.head
        i = index
        while current is not None:
            if i == 1:
                newNode = self.Node(data)
                newNode.next = current.next
                current.next = newNode
                return
            i -= 1
            current = current.next
        
        raise IndexError()

def buildOneTwoThree():
    list = LinkedList();
    list.push(3);
    list.push(2);
    list.push(1);
    return list
