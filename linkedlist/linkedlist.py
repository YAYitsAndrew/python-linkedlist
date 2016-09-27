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

def buildOneTwoThree():
    list = LinkedList();
    list.push(3);
    list.push(2);
    list.push(1);
    return list
