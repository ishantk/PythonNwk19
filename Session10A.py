"""

    DB Connectivity and SQL Execution
    ---------------------------------

    Step1: Add Library : mysql-connector in your program | To be done only once

    Step2: write SQL Statement as string in python program
    sql = "insert into Devices values (null, 'cisco_ios', 'cisco.domain.com', 'admin', 'cisco123')"

    Step3: Create Connection with DataBase
    username to database
    password to database
    host i.e. ip address where db is hosted
    database name

    Step4: Obtain Cursor Object from Connection
    used to perform SQL Operations from Python Program into DataBase

    Step5. Close Connections with Database to release memory resources

"""

import mysql.connector

def saveDevice():

    # 1. Write SQL Statement
    sql = "insert into Devices values (null, 'cisco_ios', 'cisco11.domain.com', 'admin11', '11cisco123')"

    #2. Create Connection
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

    #3. Obtain Cursor from Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()        # It ensures Multiple SQL Statements executed as Transaction
    print(">> DB Operation Finished")

    # con.close() -> becomes optional as per your requirements



def updateDevice():

    # 1. Write SQL Statement
    sql = "update Devices set username='fionna', password = 'fionna123' where id = 4"

    #2. Create Connection
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

    #3. Obtain Cursor from Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()        # It ensures Multiple SQL Statements executed as Transaction
    print(">> DB Operation Finished")

def deleteDevice():

    # 1. Write SQL Statement
    sql = "delete from Devices where id = 4"

    #2. Create Connection
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

    #3. Obtain Cursor from Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()        # It ensures Multiple SQL Statements executed as Transaction
    print(">> DB Operation Finished")


def fetchAll():

    # 1. Write SQL Statement
    # sql = "select * from Devices"
    # sql = "select * from Devices where id > 1"
    sql = "select * from Devices where username = 'john' and password = 'john123'"

    #2. Create Connection
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

    #3. Obtain Cursor from Connection
    cursor = con.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print(row)
        print(row[1], row[2])



# saveDevice()
# updateDevice()
# deleteDevice()
fetchAll()
