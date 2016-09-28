from linkedlist.linkedlist import LinkedList,  buildOneTwoThree
import pytest

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

def test_getNth():
    list = buildOneTwoThree()
    assert list.getNth(0) == 1
    assert list.getNth(1) == 2
    assert list.getNth(2) == 3
    assert list.getNth(6) == -1
    list = LinkedList()
    assert list.getNth(0) == -1
    assert list.getNth(6) == -1

def test_deleteList():
    list = buildOneTwoThree()
    list.deleteList()
    assert list.length() == 0

def test_pop():
    list = buildOneTwoThree()
    assert list.pop() == 1
    assert list.pop() == 2
    assert list.pop() == 3
    with pytest.raises(Exception): list.pop()

def test_insertNth():
    list = buildOneTwoThree()
    list.insertNth(0, 4)
    assert list.getNth(0) == 4
    assert list.length() == 4
    list.insertNth(2, 5)
    assert list.getNth(2) == 5
    assert list.length() == 5
    list.insertNth(5,  6)
    assert list.getNth(5) == 6
    assert list.length() == 6

def test_sortedInsert():
    list = buildOneTwoThree()
    list.insertNth(1,  5) #{1, 5, 2, 3}
    list.sortedInsert(list.head.next) #{1, 2, 3, 5}
    assert list.getNth(3) == 5
    list.insertNth(4,  4) #{1, 2, 3, 5, 4}
    list.sortedInsert(list.head.next.next.next.next)
    assert list.getNth(3) == 4
    list.push(6) #{6, 1, 2, 3, 4, 5}
    list.sortedInsert(list.head)
    assert list.getNth(5) == 6
    list.insertNth(5,  1) #{1, 2, 3, 4, 5, 1, 6}
    list.sortedInsert(list.head.next.next.next.next.next)
    assert list.pop() == 1
    assert list.pop() == 1
    list.insertNth(3,  1) #{2, 3, 4, 1, 5, 6}
    list.sortedInsert(list.head.next.next.next)
    assert list.pop() == 1

def test_insertSort():
    list = buildOneTwoThree()
    list.push(20)
    list.push(25)
    list.push(1)
    list.push(23)
    list.push(4)
    list.push(0)
    list.insertSort()
    assert list.pop() == 0
    assert list.pop() == 1
    assert list.pop() == 1
    assert list.pop() == 2
    assert list.pop() == 3
    assert list.pop() == 4
    assert list.pop() == 20
    assert list.pop() == 23
    assert list.pop() == 25
    assert list.length() == 0

def test_append():
    list1 = buildOneTwoThree()
    list2 = buildOneTwoThree()
    list1.append(list2)
    assert list1.length() == 6
    assert list2.length() == 0
    list1 = LinkedList()
    list2 = buildOneTwoThree()
    list1.append(list2)
    assert list1.length() == 3
    assert list2.length() == 0
    list1.append(list2)
    assert list1.length() == 3
    assert list2.length() == 0

def test_frontBackSplit():
    list = buildOneTwoThree()
    node1,  node2 = list.frontBackSplit()
    assert node1.data == 1
    assert node2.data == 3
    list = LinkedList()
    node1,  node2 = list.frontBackSplit()
    assert node1 is None
    assert node2 is None
    list.push(1)
    node1,  node2 = list.frontBackSplit()
    assert node1.data == 1
    assert node2 is None
