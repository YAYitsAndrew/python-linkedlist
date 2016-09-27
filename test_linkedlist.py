from linkedlist.linkedlist import LinkedList,  buildOneTwoThree

def test_buildOneTwoThree():
    list = buildOneTwoThree()
    
    current = list.head
    assert current.data == 1
    
    current = current.next
    assert current.data == 2
    
    current = current.next
    assert current.data == 3

def test_length():
    list = LinkedList()
    assert list.length() == 0
    
    list.push(0)
    assert list.length() == 1
    
    list = buildOneTwoThree()
    assert list.length() == 3

def test_count():
    list = buildOneTwoThree()
    
    assert list.count(2) == 1
    assert list.count(5) == 0
    
    list.push(2)
    assert list.count(2) == 2
