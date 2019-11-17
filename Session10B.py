import mysql.connector

# OOPS
class Device:

    def __init__(self,  deviceType, host, username, password):
        self.deviceType = deviceType
        self.host = host
        self.username = username
        self.password = password

    def showDevice(self):
        print(">> Device Details: {} {} {} {}".format(self.deviceType, self.host, self.username,
                                                      self.password))

    def getDataForDeviceFromUser(self):
        self.deviceType = input("Enter Device Type: ")
        self.host = input("Enter Device Host: ")
        self.username = input("Enter Device Username: ")
        self.password = input("Enter Device Password: ")

    def saveDevice(self):
        # 1. Write SQL Statement
        sql = "insert into Devices values (null, '{}', '{}', '{}', '{}')".format(
            self.deviceType, self.host, self.username, self.password)

        # 2. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor from Connection
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()  # It ensures Multiple SQL Statements executed as Transaction
        print(">> {} Device Saved".format(self.deviceType))

    def fetchAll(self):
        # 1. Write SQL Statement
        sql = "select * from Devices"

        # 2. Create Connection
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor from Connection
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)


"""
device = Device(None, None, None, None)
device.getDataForDeviceFromUser()
device.showDevice()

# After Line#23 Data Entered by User in Object is LOST
# If its has to be saved i.e. persisted, we got 2 options
# 1. Files
# 2. DataBase

choice = input("Would you like to save Device(yes/no): ")
if choice == "yes":
    device.saveDevice()

# Other Operations : Update, Delete and Fetch -> Integrate Yourself
"""

device = Device(None, None, None, None)
device.fetchAll()