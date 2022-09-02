

class atmController():
    def __init__(self):
        self.cardStatus = 0
        self.pinNumber = "0000"
        self.account = "1234567"
        self.balance = 0
        self.deposit = 0
        self.withdraw = 0

    def InsertCard(self, card):
        pass

    def PINnumber(self, pin):
        pass

    def SelectAccount(self, account):
        pass

    def ShowAccountInfo(self):
        return self.balance, self.deposit, self.withdraw