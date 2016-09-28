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
    
    #6
    def sortedInsert(self,  node):
        #remove node from old position
        #head special case
        if self.head == node:
            self.head = node.next
            node.next = None
        
        #walk through and find node to remove
        current = self.head
        while current is not None:
            if current.next == node:
                current.next = node.next;
                node.next = None
                break
            current = current.next
        
        #find new position
        #head special case
        if self.head.data > node.data:
            node.next = self.head
            self.head = node
            return
        
        #walk through and find insert spot
        current = self.head
        last = None
        while current is not None:
            if current.data > node.data and last.data <= node.data:
                last.next = node
                node.next = current
                break
            last = current;
            current = current.next
        
        #no spot found, must go on the end
        if node.next is None:
            last.next = node
    
    #7
    def insertSort(self):
        unvisited = []
        current = self.head
        while current is not None:
            unvisited.append(current)
            current = current.next
        
        for node in unvisited:
            self.sortedInsert(node)
    
    #8
    def append(self,  list2):
        current = self.head
        if current is None: #empty first list case
            self.head = list2.head
        else: #find the last node
            while current.next is not None:
                current = current.next
            current.next = list2.head
        list2.head = None
    
    #9
    def frontBackSplit(self):
        len = self.length()
        if len == 0:
            return [None,  None]
        
        len1 = len - (len // 2)
        current = self.head
        for i in range(0,  len1 - 1):
            current = current.next
        #now current is the last node of the front half
        return [self.head,  current.next]

def buildOneTwoThree():
    list = LinkedList();
    list.push(3);
    list.push(2);
    list.push(1);
    return list
