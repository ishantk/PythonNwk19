# API: Application Programming Interfaces
#      Built in code which we will use to meet objectives

# import datetime
import datetime as dt

today = dt.datetime.today()
print(">> Its:", today)

tomorrow = dt.datetime(2019, 11, 3, 12, 45, 0)
print(">> Tomorrow is:", tomorrow)

diff = tomorrow - today
print(">> Difference:", diff)


