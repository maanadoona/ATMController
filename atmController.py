from enum import Enum


class CardStatus(Enum):
    NotInserted = 0
    Inserted = 1

class PinStatus(Enum):
    Incorrect = 0
    Correct = 1

class AccountStatus(Enum):
    NotSelected = 0
    Selected = 1

class AtmController():
    def __init__(self):
        self.cardStatus = CardStatus.NotInserted
        self.pinNumber = "0000"
        self.pinStatus = PinStatus.Incorrect
        self.account = "1234567"
        self.accountStatus = AccountStatus.NotSelected
        self.balance = 0
        self.deposit = 0
        self.withdraw = 0

    def InsertCard(self, card):
        self.cardStatus = card
        pass

    def PINnumber(self, pin):
        # PIN Number Rule Check
        if len(pin) != 4:   # 1) size : 4
            self.pinStatus = PinStatus.Incorrect
        else:               # 2) 0~9
            if pin.isdigit() is False:
                self.pinStatus = PinStatus.Incorrect
            else:
                self.pinStatus = PinStatus.Correct
                self.pinNumber = pin

    def SelectAccount(self, account):
        pass

    def ShowAccountInfo(self):
        return self.balance, self.deposit, self.withdraw