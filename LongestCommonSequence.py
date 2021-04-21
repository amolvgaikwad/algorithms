def LongestCommonSequence(firstValue, secondValue):
    firstValueLength = len(firstValue)
    secondValueLength = len(secondValue)
    L = [[0 for x in range(secondValueLength+1)] for x in range(firstValueLength+1)]

    for indexFirstValue in range(firstValueLength+1):
        for indexSecondValue in range(secondValueLength+1):
            if indexFirstValue == 0 or indexSecondValue == 0:
                L[indexFirstValue][indexSecondValue] = 0
            elif firstValue[indexFirstValue-1] == secondValue[indexSecondValue-1]:
                L[indexFirstValue][indexSecondValue] = L[indexFirstValue-1][indexSecondValue-1] + 1
            else:
                L[indexFirstValue][indexSecondValue] = max(L[indexFirstValue-1][indexSecondValue], L[indexFirstValue][indexSecondValue-1])

    index = L[firstValueLength][secondValueLength]
    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""
    _firstValueLength = firstValueLength
    _secondValueLength = secondValueLength

    while _firstValueLength > 0 and _secondValueLength > 0 and _firstValueLength < 50 and _secondValueLength < 50:
        if firstValue[_firstValueLength-1] == secondValue[_secondValueLength-1]:
            lcs_algo[index-1] = firstValue[_firstValueLength-1]
            _firstValueLength -= 1
            _secondValueLength -= 1
            index -= 1
        elif L[_firstValueLength-1][_secondValueLength] > L[_firstValueLength][_secondValueLength-1]:
            _firstValueLength -= 1
        else:
            _secondValueLength -= 1

    print("".join(lcs_algo))

# Based on both inputs  LongestCommonSequence method will identify the matching pattern
userInputString = input("Enter the Semicolon Seperated string: ")   
splittedUserInputString = userInputString.split(';')
firstValue = splittedUserInputString[0]
secondValue = splittedUserInputString[1]
LongestCommonSequence(firstValue, secondValue)