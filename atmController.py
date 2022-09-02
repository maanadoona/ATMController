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
        self.account = "123-4567"
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
        # Account Rule Check
        if len(account) != 7:   # 1) size : 8
            self.accountStatus = AccountStatus.NotSelected
        else:
            if account[3] != '-':   # 2) hyphen check
                self.accountStatus = AccountStatus.NotSelected
            else:
                accFormer = account[:2]
                if accFormer.isdigit() is False:    # 3) Former Num check
                    self.accountStatus = AccountStatus.NotSelected
                else:
                    accLast = account[4:]
                    if accLast.isdigit() is False:  # 4) Last Num check
                        self.accountStatus = AccountStatus.NotSelected
                    else:   # Okay
                        self.accountStatus = AccountStatus.Selected
                        self.account = account

    def ShowAccountInfo(self):
        return self.balance, self.deposit, self.withdraw