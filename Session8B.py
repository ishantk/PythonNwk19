# By Default whatever python file you are creating is known as a Module

appName = "==Zomato=="

def applyPromoCode(promoCode, amount):
    print(">> Promo Code {} Successfully Applied on Amount {}".format(promoCode, amount))

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def show(self):
        print(">> Student Details:",self.roll," | ",self.name)