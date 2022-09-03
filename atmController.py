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
        self.pinNumber = "1234"
        self.pinStatus = PinStatus.Incorrect
        self.account = "123-4567"
        self.accountStatus = AccountStatus.NotSelected
        self.balance = 700
        self.deposit = 1000
        self.withdraw = 300

    def InsertCard(self, card):
        print("[STEP1] Insert Card")
        self.cardStatus = card

        return self.ShowCardStatus(self.cardStatus)

    def PINnumber(self, pin):
        print("[STEP2] PIN number")
        if self.cardStatus == CardStatus.NotInserted:
            return self.ShowCardStatus(CardStatus.NotInserted)
        else:
            # PIN Number Rule Check
            if len(pin) != 4:   # 1) size : 4
                self.pinStatus = PinStatus.Incorrect
            else:               # 2) 0~9
                if pin.isdigit() is False:
                    self.pinStatus = PinStatus.Incorrect
                else:
                    if pin != self.pinNumber:   # 3) PIN code wrong
                        self.pinStatus = PinStatus.Incorrect
                    else:
                        self.pinStatus = PinStatus.Correct
                        self.pinNumber = pin

            return self.ShowPinStatus(self.pinStatus)

    def SelectAccount(self, account):
        print("[STEP3] Select Account")
        if self.cardStatus == CardStatus.NotInserted:
            return self.ShowCardStatus(CardStatus.NotInserted)
        elif self.pinStatus == PinStatus.Incorrect:
            return self.ShowPinStatus(PinStatus.Incorrect)
        else:
            # Account Rule Check
            if len(account) != 8:   # 1) size : 8
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
                            print("[STEP4] See Balance/Deposit/Withdraw")
                            b, d, w = self.ShowAccountInfo()
                            print(b, d, w)

            return self.ShowSelectAccount(self.accountStatus)
    
    def ShowAccountInfo(self):
        return self.balance, self.deposit, self.withdraw

    def ShowCardStatus(self, status):
        if status == CardStatus.NotInserted:
            return "Please, Insert Card."
        elif status == CardStatus.Inserted:
            return "Card Detected, Please Input the pincode."

    def ShowPinStatus(self, status):
        if status == PinStatus.Incorrect:
            return "Invalid Pincode, Try Again."
        elif status == PinStatus.Correct:
            return "Valid Pincode, Select Account Please."

    def ShowSelectAccount(self, status):
        if status == AccountStatus.NotSelected:
            return "Wrong Account Number, Check your Account again."
        elif status == AccountStatus.Selected:
            return "Okay. Please wait a second."


# Test 1 : Normal Case
atm = AtmController()
ret = atm.InsertCard(CardStatus.Inserted)
print(ret)
ret = atm.PINnumber("1234")
print(ret)
ret = atm.SelectAccount("123-4567")
print(ret)


'''
# Test 2 : Card isn't inserted
atm = AtmController()
ret = atm.InsertCard(CardStatus.NotInserted)
print(ret)
# ret = atm.InsertCard(CardStatus.Inserted)
# print(ret)
ret = atm.PINnumber("1234")
print(ret)
ret = atm.SelectAccount("123-4567")
print(ret)
'''

'''
# Test 3 : Pincode Passing
atm = AtmController()
#ret = atm.InsertCard(CardStatus.NotInserted)
#print(ret)
ret = atm.InsertCard(CardStatus.Inserted)
print(ret)
#ret = atm.PINnumber("1234")
#print(ret)
ret = atm.SelectAccount("123-4567")
print(ret)
ret = atm.PINnumber("1234")
print(ret)
ret = atm.SelectAccount("123-4567")
print(ret)
'''