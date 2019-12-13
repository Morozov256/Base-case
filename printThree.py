def binThreePrint(node):
    '''
    Example of recursion
    The method returns string of node values of binary three in order (i.e. left-root-right)
    :param node: binary tree in a list format [node, [left-three], [right-three]]
    :return: string of node values of binary three in order
    '''
    mystr = ''
    if node[1]:
        mystr += str(binThreePrint(node[1]))
    mystr += str(node[0])
    if node[2]:
        mystr += str(binThreePrint(node[2]))
    return mystr