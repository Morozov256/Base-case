def startChanging(string, symbol):
    '''
    The method for start.
    Prints all possible options to replace each of the specified characters in the string
    with the remaining characters in the string
    :param string: the string for replacing
    :param symbol: the specified character
    :return: nothing
    '''
    #global letters_set  # set of letters
    if symbol in string:
        result = []  # list of result words
        letters_set = set(string)
        letters_set.remove(symbol)  # exclude specified characters
        ChangeSymbol(string, letters_set, result, symbol)
        result = sorted(result)  # for easy read result
        for i in result:  # print result into column
            print(i)
    else:
        print(string)

def ChangeSymbol(string, letters_set, result, symbol):
    '''
    The method add string to result list if it string is not contains stars
    :param string: string as a string or list of characters
    :param letters_set: the remaining characters in the string
    :param result: list of final words (without the specified characters)
    :param symbol: the specified character
    :return: nothing
    '''
    tmp = list(string)  # for prevent changing data
    index = FindSymbol(tmp, symbol)

    if index < 0:
        res = ''
        for i in range(len(tmp)):
            res += tmp[i]  # turn list of characters to string
        result.append(res)
    else:
        for i in letters_set:  # for each letter in the set
            tmp[index] = i
            ChangeSymbol(tmp, letters_set, result, symbol)  # recursion

def FindSymbol(string, symbol):
    '''
    The method find index of first specified character (symbol) in the string
    :param string: string as a list of characters
    :param symbol: the specified character
    :return: index of first specified character (symbol) in the string or -1 if it not found
    '''
    for i in range(len(string)):
        if string[i] == symbol:
            return i
    return -1