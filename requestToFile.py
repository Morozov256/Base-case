def requestToFile(cursor, sql, fileName='output.txt'):
    '''
    The method creates the file (fileName) and it create a report based on the given sql statement.
    The report visually create a table, containing as the first row the Column names (center aligned).
    Each column will be of size 20, each string field will be cut to fit this size,
    all values will be center aligned except integers that will be right align.

    integer types: 1,2,3,8,9,13,16

    :param cursor: connection with database
    :param sql: string as sql statement
    :param fileName: file for writing the table, by default 'output.txt'
    :return: nothing
    '''
    cursor.execute(sql)
    columnTypes = [col[1] for col in cursor.description]  # list of the data types

    with open(fileName, 'w') as resFile:  # clean file
        resFile.write('')
        resFile.close()


    with open(fileName, 'a') as f:
        f.write('-' * (21 * len(columnTypes) + 1) + '\n')
        f.write('|' + '|'.join('{:^20s}'.format(col[0]) for col in cursor.description) + '|\n')  # create a titles line
        f.write('-' * (21 * len(columnTypes) + 1) + '\n')
        rows = cursor.fetchmany(100)
        while len(rows) > 0:
            for row in rows:
                f.write('|' + '|'.join
                ('{:>20s}'.format(str(row[i]))
                 if columnTypes[i] in [1, 2, 3, 8, 9, 13, 16]  # checking if data type is an integer type
                 else '{:^20s}'.format(str(row[i]))
                 for i in range(len(row))) + '|\n')
                f.write('-' * (21 * len(columnTypes) + 1) + '\n')
            rows = cursor.fetchmany(100)
        f.close()

def createCursor(db, host='localhost', user='root', password=''):
    '''
    The method just helps to create the cursor
    :param db: name of data base
    :param host: address of server, by default 'localhost'
    :param user: user name, by default 'root'
    :param password: password, by default ''
    :return: cursor
    '''
    import pymysql
    db = pymysql.connect(host, user, password, db)
    db.autocommit(True)
    return db.cursor()

'''
Example of using:

cursor = createCursor('employees')
sql = 'Select * from employees'
requestToFile(cursor, sql)
'''