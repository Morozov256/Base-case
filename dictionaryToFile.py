def dictionaryToFile (inputFileName, outputFileName = 'output.txt', sorted=False):
    '''
    This method creates a dictionary of words that are used in the input file,
    calculates their number, and writes the information to the output file.

    :param inputFileName: string, name of input file
    :param outputFileName: string, name of output file, 'output.txt' by default
    :param sorted: boolean, if it is true, then the dictionary will be sorted, False by default
    :return: nothing
    '''
    import re  # we will use regexp
    listWords = {}  # create a dictionary

    with open(inputFileName, 'r') as f:  # open the input file for reading
        for line in f:  # read the file by line
            # split line
            listLine = filter(lambda x: x != '', re.split('[ ,.:;"?!%()\[\]{}\-\'\t\n\d]+', line.lower()))
            for item in listLine:
                if listWords.get(item) != None:  # if key is exist, increase it
                    listWords[item] = int(listWords.get(item))+1
                else:  # if key is exist, create it with value 1
                    listWords.setdefault(item, 1)
    f.close()  # close reading stream

    if sorted:  # if we want to have result as sorted list
        tmpList = []
        for key in listWords:
            tmpList.append(key)
        tmpList.sort()

        with open(outputFileName, 'w') as f:  # open the output file for writing
            for key in tmpList:
                f.write(key+': '+str(listWords[key])+'\n')
        f.close()  # close writing stream

    else:  # if we do not want to have result as sorted list

        with open(outputFileName, 'w') as f:  # open the output file for writing
            for key in listWords.keys():
                f.write(key+': '+str(listWords[key])+'\n')
        f.close()  # close writing stream