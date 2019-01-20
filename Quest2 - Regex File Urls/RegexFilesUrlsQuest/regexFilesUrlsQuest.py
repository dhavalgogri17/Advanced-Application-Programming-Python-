#Quest: Regex, Files, Urls

import re
import requests


__STUDENT_ID__  = "47444609"        # replace with your 8 digit student id
__QUEST_NAME__ = "Code "           # replace with your coding name - max 15 characters

def count_vowels(mystr):
    matchObject = re.findall(r'[aeiou]', mystr, re.IGNORECASE)
    return matchObject.__len__()


def is_valid_python_hex(mystr):
    matchObject = re.search(r'^(0{1}x{1})[A-F0-9]+$', mystr, re.IGNORECASE)
    if matchObject:
        return True
    else:
        return False

def has_vowel(mystr):
    matchObject = re.search(r'[aeiou]', mystr, re.IGNORECASE)
    if matchObject:
        return True
    else:
        return False


def is_integer(mystr):
    matchObject = re.search(r'^(-?)[0-9]+$', mystr, re.IGNORECASE)
    if matchObject:
        return True
    else:
        return False


def get_extension(mystr):
    matchObject = re.search(r'^[a-z].*[.]{1}[a-z]+$', mystr, re.IGNORECASE)
    if matchObject:
        return ('' + re.findall(r'[a-z]*$', mystr, re.IGNORECASE)[0])
    else:
        return 'NONE'

def is_number(mystr):
    matchObject = re.search(r'^(-?)[0-9]+?[.]{0,1}[0-9]*$', mystr, re.IGNORECASE)
    if matchObject:
        return True
    else:
        return False

    return True

def convert_date_format(mystr):
    matchObject = re.search(r'^(\d{4})-(\d{1,2})-(\d{1,2})$', mystr, re.IGNORECASE)
    if matchObject:
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\2-\\3-\\1', mystr)
    else:
        return 'NONE'


#File functions
def readFileCountLines(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        print(data)
        matchObject = re.findall(r'\n', data, re.IGNORECASE)
        print(matchObject.__len__() + 1)
        return (matchObject.__len__() + 1)



def readFileCountStringOccurrences(filename, stringval):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        matchObject = re.findall(r'(' + re.escape(stringval) + ')', data, re.IGNORECASE)
        print(matchObject)
        return matchObject.__len__()

def readFileSumDigitsGreaterThanNumber(filename, number):
    with open(filename, 'r') as myfile:
        data = myfile.read()
        matchObject = re.findall(r'\d[0-9]+', data, re.IGNORECASE | re.MULTILINE)
        print(matchObject)
        sum = 0
        for allNumbers in matchObject:
            if int(allNumbers) > number:
                sum = sum + int(allNumbers)
        return sum


def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    matchObject = re.findall(r'[a-z]+', mystr, re.IGNORECASE)
    print(matchObject)
    if matchObject:
        allAplha = ""
        for alpha in matchObject:
            allAplha = allAplha + alpha
        return allAplha
    else:
        return 'NONE'


#URL functions
def readurlCountStringOccurrences(urlname, stringval):
    response = requests.get(urlname)
    matchObject = re.findall(r'(' + re.escape(stringval) + ')', response.content.decode('utf-8'), re.IGNORECASE)
    if matchObject:
        return matchObject.__len__()

    return 0


def readurlCountValidPhoneNumbers(urlname):
    response = requests.get(urlname)
    matchObject = re.findall(r'([0-9]{3}[.][0-9]{3}[.][0-9]{4})|([0-9]{3}[-][0-9]{3}[-][0-9]{4})|([0-9]{10})', response.content.decode('utf-8'), re.IGNORECASE)
    if matchObject:
        return matchObject.__len__()

    return 0



if __name__  == '__main__':
    print ("To test your code execute: python test_QuestFilesUrls.py  or on command line execute: pytest ")



