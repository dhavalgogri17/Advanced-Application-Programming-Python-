# Testfile for basicPythonQuest.py
import pytest
import basicPythonQuest 


# TESTS   

def test_isSorted1():
    assert basicPythonQuest.isSorted([2, 4, 7, 7, 99, 122]) == True


def test_isSorted2():
    assert basicPythonQuest.isSorted(['a', 'b', 'c']) == True


def test_isSorted3():
    assert basicPythonQuest.isSorted(['a', 'z', 'b', 'c']) == False


def test_isSortedAndUnique1():
    assert basicPythonQuest.isSortedAndUnique([2, 4, 7, 7, 99, 122]) == False


def test_isSortedAndUnique2():
    assert basicPythonQuest.isSortedAndUnique(['a', 'b', 'c']) == True


def test_isSortedAndUnique3():
    assert basicPythonQuest.isSortedAndUnique(['a', 'z', 'b', 'b', 'c']) == False


def test_hasUniqueValues1():
    assert basicPythonQuest.hasUniqueValues([2, 4, 7, 99, 122, 7]) == False


def test_hasUniqueValues2():
    assert basicPythonQuest.hasUniqueValues(['a', 'b', 'c']) == True


def test_hasUniqueValues3():
    assert basicPythonQuest.hasUniqueValues(['a', 'z', 'b', 'b', 'c']) == False

def test_genSortedArrayUniqueValues1():
    assert basicPythonQuest.genSortedArrayUniqueValues(['a','b','z','c', 'a']) ==  ['a','b','c','z']

def test_genSortedArrayUniqueValues2():
    assert basicPythonQuest.genSortedArrayUniqueValues([2,4,7,7,122,99]) ==  [2,4,7,99,122]

def test_listToMapTwoByTwo1():
    assert basicPythonQuest.listToMapTwoByTwo(['foo', 'bar']) == {'foo': 'bar'}


def test_listToMapTwoByTwo2():
    assert basicPythonQuest.listToMapTwoByTwo(['a', 2, 3, 'foo']) == {'a': 2, 3: 'foo'}


def test_listToMapTwoByTwo3():
    assert basicPythonQuest.listToMapTwoByTwo([]) == {}


def test_wordsInStringToDictWordCount1():
    assert basicPythonQuest.wordsInStringToDictWordCount('foo bar   bar') == {'foo': 1, 'bar': 2}


def test_wordsInStringToDictWordCount2():
    assert basicPythonQuest.wordsInStringToDictWordCount('') == {}


def test_reverseWordsInString1():
    assert basicPythonQuest.reverseWordsInString('foo bar bar baz') == 'baz bar bar foo'


def test_genListOfOverlaps1():
    assert basicPythonQuest.genListOfOverlaps([2, 4, 6, 8], [6, 2, 2, 9, 7]) == [2, 6]


def test_genListOfOverlaps2():
    assert basicPythonQuest.genListOfOverlaps([2, 4, 6, 8], [2, 4, 6, 8]) == [2, 4, 6, 8]


def test_genListOfOverlaps3():
    assert basicPythonQuest.genListOfOverlaps([2, 4, 6, 8], [1, 1, 9, 7]) == []


def test_removeDupsNoSet1():
    assert basicPythonQuest.removeDupsNoSet([1, 1, 2, 2, 5, 6]) == [1, 2, 5, 6]


def test_removeDupsUseSet1():
    assert basicPythonQuest.removeDupsUseSet([1, 1, 2, 2, 5, 6]) == [1, 2, 5, 6]



if __name__ == '__main__':
    print("running main ")
    pytest.main()
    

