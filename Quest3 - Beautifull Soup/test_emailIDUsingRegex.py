# Testfile for basicPythonQuest.py
import pytest
import basicPythonQuest


# TESTS

def test_checkEmail1():
    assert checkEmailRegex.checkEmail('dhaval.gogri17@gmail.com') == True


def test_checkEmail2():
    assert checkEmailRegex.checkEmail('dgogri@smu.edu') == True


def test_checkEmail3():
    assert checkEmailRegex.checkEmail('dhaval.gogri17@gmail.org') == True


def test_checkEmail4():
    assert checkEmailRegex.checkEmail('dhaval.gogri17@gmail.com_') == False

def test_checkEmail5():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17@gmail.com') == False

def test_checkEmail6():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17.@gmail.com') == False

def test_checkEmail7():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17@_gmail.com') == False

def test_checkEmail8():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17@gmail_.com') == False

def test_checkEmail9():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17@gmail.con') == False

def test_checkEmail10():
    assert checkEmailRegex.checkEmail('.dhaval.gogri17@gmail.edum') == False


if __name__ == '__main__':
    print("running main ")
    pytest.main()


