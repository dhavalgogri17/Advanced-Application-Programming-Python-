
# Testfile for ", regexFilesUrlsQuest.py

import regexFilesUrlsQuest as Reg
import re, pytest, os

def getTotalTestCount():
    f = open(os.path.basename(__file__), 'r')
    lines = f.read()
    resList = re.findall(r'^def test_', lines, re.M)
    return len(resList)

def init():
    # get test & user-specific info  -------------- 
    tt   = getTotalTestCount()
    id   = Reg.__STUDENT_ID__
    name = Reg.__QUEST_NAME__
    cat  = 'Reg'
    return (id,name,cat,tt)

#TESTS

def test_IdIsEightDigits():
    assert re.match(r'\d{8}',Reg.__STUDENT_ID__) != None

def test_okQuestName():    
    assert Reg.__QUEST_NAME__ != 'undef'  and len(Reg.__QUEST_NAME__) < 7


def test_count_vowels1():
	assert Reg.count_vowels('aaacvemmikkOOzzuU')==9

def test_is_valid_python_hex1():
	assert Reg.is_valid_python_hex('0x1A2f')==True

def test_is_valid_python_hex2():
	assert Reg.is_valid_python_hex('x1A2f')==False

def test_is_valid_python_hex3():
	assert Reg.is_valid_python_hex('0x1A2G')==False

def test_has_vowel1():
	assert Reg.has_vowel("zcxvsd")==False

def test_has_vowel2():
	assert Reg.has_vowel("vcbxvefjk")==True

def test_is_integer1():
	assert Reg.is_integer("2345")==True

def test_is_integer2():
	assert Reg.is_integer("-192345")==True

def test_is_integer3():
	assert Reg.is_integer("234x5")==False

def test_get_extension1():
	assert Reg.get_extension('foo.zip')=='zip'

def test_get_extension2():
	assert Reg.get_extension('foo.doc.txt')=='txt'

def test_get_extension3():
	assert Reg.get_extension('foozip')=='NONE'

def test_is_number1():
	assert Reg.is_number('234')==True

def test_is_number2():
	assert Reg.is_number('-234')==True

def test_is_number3():
	assert Reg.is_number('234.')==True

def test_is_number4():
	assert Reg.is_number('234.999')==True

def test_is_number5():
	assert Reg.is_number('234.99.77')==False

def test_is_number6():
	assert Reg.is_number('234a.88')==False

def test_convert_date_format1():
	assert Reg.convert_date_format('2018-03-04')=='03-04-2018'

def test_convert_date_format2():
	assert Reg.convert_date_format('2018.03-04')=='NONE'

def test_convert_date_format3():
	assert Reg.convert_date_format('2018-03-054')=='NONE'

def test_readFileCountLines1():
	assert Reg.readFileCountLines('pytestFile1.txt')==4

def test_readFileCountStringOccurrences1():
	assert Reg.readFileCountStringOccurrences('pytestFile1.txt','rollo')==3

def test_readFileSumDigitsGreaterThanNumber1():
	assert Reg.readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)==88

def test_remove_all_but_alpha1():
	assert Reg.remove_all_but_alpha('hey-99-where8isthe**big_table**')=='heywhereisthebigtable'

def test_readurlCountStringOccurrences1():
	assert Reg.readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')==3

def test_readurlCountValidPhoneNumbers1():
	assert Reg.readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')==3

   

if __name__  == '__main__':
    print ("Processing test results...")

    initTup = init()

    #RUN TESTS   
    pytest.main()



