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
