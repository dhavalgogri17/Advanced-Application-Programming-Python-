# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__  = "47444609"     # replace with your 8 digit student id
__CODING_NAME__ = "Code Gladiator"        # replace with your coding name -

def isSorted(list):
    isListSorted = True 
    for i in range(1, len(list)):
        if (list[i] < list[i-1]):
            return False 
    return isListSorted 


def isSortedAndUnique(list):
    isListSortedAndUnique = True 
    for i in range(1, len(list)):
        if (list[i] <= list[i - 1]):
            return False 
    return isListSortedAndUnique 


def hasUniqueValues(list):
    hasUniqueValues = True 
    dict = {}
    for i in range(0, len(list)):
        if list[i] in dict:
            return False
        else:
            dict[list[i]] = 1
    return hasUniqueValues


def genSortedArrayUniqueValues(list):
    for i in range(0, len(list) - 1):
        for j in range(i+1, len(list) - 1):
            if (list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]

    sortedUniqueArray = []
    sortedUniqueArray.append(list[0])
    for i in range(0, len(list)):
        if (list[i] > list[i - 1]):
            sortedUniqueArray.append(list[i])
    return sortedUniqueArray


def listToMapTwoByTwo(list):
    dict = {}
    for i in range(0, len(list) - 1 , 2):
        dict[list[i]] = list[i + 1]
    return dict

def wordsInStringToDictWordCount(s):
    splitWords = s.split()
    dict = {}
    for i in range(0, len(splitWords)):
        if splitWords[i] in dict:
            dict[splitWords[i]] = dict.get(splitWords[i]) + 1  
        else:
            dict[splitWords[i]] = 1
    return dict


def reverseWordsInString(string):
    splitWords = string.split()
    reverseString = splitWords[len(splitWords) - 1]
    for i in range(len(splitWords) - 2, -1, -1):
        reverseString = reverseString + " " + splitWords[i]
    return reverseString



def genListOfOverlaps(list1, list2):
    overlappingLists = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if(list1[i] == list2[j]):
                overlappingLists.append(list1[i])
                break

    return genSortedArrayUniqueValues(overlappingLists)


def removeDupsNoSet(list):
    dict = {}
    noDuplicateSet = []
    for i in range(0, len(list)):
        if list[i] in dict:
            dict[list[i]] = dict.get(list[i]) + 1  
        else:
            dict[list[i]] = 1
    for key in dict.keys():
        noDuplicateSet.append(key)
    return noDuplicateSet


def removeDupsUseSet(list1):
    return list(set(list1))

if __name__ == '__main__':
    print ('ready to go')