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
        self.PINNUM_LEN = 4
        self.ACCOUNT_LEN = 8
        self.ACCOUNT_HYPHEN = 3
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
            return self.ShowCardStatus(self.cardStatus)
        else:
            # PIN Number Rule Check
            if len(pin) != self.PINNUM_LEN:   # 1) size : 4
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
            return self.ShowCardStatus(self.cardStatus)
        elif self.pinStatus == PinStatus.Incorrect:
            return self.ShowPinStatus(self.pinStatus)
        else:
            # Account Rule Check
            if len(account) != self.ACCOUNT_LEN:   # 1) size : 8
                self.accountStatus = AccountStatus.NotSelected
            else:
                if account[self.ACCOUNT_HYPHEN] != '-':   # 2) hyphen check
                    self.accountStatus = AccountStatus.NotSelected
                else:
                    accountLeft = account[:self.ACCOUNT_HYPHEN]
                    if accountLeft.isdigit() is False:    # 3) Left Num check
                        self.accountStatus = AccountStatus.NotSelected
                    else:
                        accountRight = account[self.ACCOUNT_HYPHEN+1:]
                        if accountRight.isdigit() is False:  # 4) Right Num check
                            self.accountStatus = AccountStatus.NotSelected
                        else:   # Okay
                            if self.account != account:
                                self.accountStatus = AccountStatus.NotSelected
                            else:
                                self.accountStatus = AccountStatus.Selected
                                self.account = account

            return self.ShowSelectAccount(self.accountStatus)

    def SeeAccount(self):
        print("[STEP4] See Balance/Deposit/Withdraw")
        if self.cardStatus == CardStatus.NotInserted:
            return self.ShowCardStatus(self.cardStatus)
        elif self.pinStatus == PinStatus.Incorrect:
            return self.ShowPinStatus(self.pinStatus)
        elif self.accountStatus == AccountStatus.NotSelected:
            return self.ShowSelectAccount(self.accountStatus)
        else:
            b, d, w = self.GetAccountInfo()
            print("* Your Account {%s} Information *" %(self.account))
            print("* Balance : %d dollar(s)" %(b))
            print("* Deposit : %d dollar(s)" %(d))
            print("* Withdraw : %d dollar(s)" %(w))

        return b, d, w

    def GetAccountInfo(self):
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

'''
# Test 1 : Normal Case
atm = AtmController()
ret = atm.InsertCard(CardStatus.Inserted)
print(ret)
ret = atm.PINnumber("1234")
print(ret)
ret = atm.SelectAccount("123-4567")
print(ret)
ret = atm.SeeAccount()
print(ret)
'''

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
ret = atm.SeeAccount()
print(ret)
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

ret = atm.SelectAccount("13m-3232")
print(ret)
ret = atm.SeeAccount()
print(ret)

ret = atm.SelectAccount("133-k235")
print(ret)
ret = atm.SeeAccount()
print(ret)

ret = atm.SelectAccount("133-723g")
print(ret)
ret = atm.SeeAccount()
print(ret)

ret = atm.SelectAccount("133-7235")
print(ret)
ret = atm.SeeAccount()
print(ret)

ret = atm.SelectAccount("123-4567")
print(ret)
ret = atm.SeeAccount()
print(ret)

