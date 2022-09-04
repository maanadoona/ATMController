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


class AccountInfo:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposit = 0
        self.withdraw = 0

    def Deposit(self, d):
        self.deposit += d
        self.balance = self.deposit - self.withdraw

    def Withdraw(self, w):
        self.withdraw += w
        self.balance = self.deposit - self.withdraw

    def GetInfo(self):
        return self.balance, self.deposit, self.withdraw


class AtmController:
    def __init__(self):
        self.PINNUM_LEN = 4
        self.ACCOUNT_LEN = 8
        self.ACCOUNT_HYPHEN = 3
        self.cardStatus = CardStatus.NotInserted
        self.pinNumber = "1234"
        self.pinStatus = PinStatus.Incorrect
        self.accountStatus = AccountStatus.NotSelected
        self.account = ""
        self.account1 = AccountInfo("123-4567")
        self.account1.Deposit(1000)
        self.account1.Withdraw(500)
        self.account2 = AccountInfo("111-2222")
        self.account2.Deposit(2000)
        self.account2.Withdraw(300)
        self.account3 = AccountInfo("333-4444")
        self.account3.Deposit(500)
        self.account3.Withdraw(20)

        self.accountList = [self.account1, self.account2, self.account3]

    def InsertCard(self, card):
        print("[STEP1] Insert Card : %s" %(card))
        if card == "INSERT":
            self.cardStatus = CardStatus.Inserted
        elif card == "REJECT":
            self.cardStatus = CardStatus.NotInserted
        else:
            self.cardStatus = CardStatus.NotInserted
            return card + ":WRONG MSG"

        return self.ShowCardStatus(self.cardStatus)

    def PINnumber(self, pin):
        print("[STEP2] PIN number : %s" %(pin))
        if self.cardStatus == CardStatus.NotInserted:
            self.pinStatus = PinStatus.Incorrect
            self.accountStatus == AccountStatus.NotSelected
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

        if self.pinStatus == PinStatus.Incorrect:
            return self.ShowPinStatus(self.pinStatus)
        else:
            return self.ShowPinStatus(self.pinStatus) + " " + str([a.name for a in self.accountList])

    def SelectAccount(self, account):
        print("[STEP3] Select Account : %s" %(account))
        if self.cardStatus == CardStatus.NotInserted:
            self.pinStatus = PinStatus.Incorrect
            self.accountStatus = AccountStatus.NotSelected
            return self.ShowCardStatus(self.cardStatus)
        elif self.pinStatus == PinStatus.Incorrect:
            self.accountStatus == AccountStatus.NotSelected
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
                            for a in self.accountList:
                                if account == a.name:
                                    self.accountStatus = AccountStatus.Selected
                                    self.account = a
                                    break
                            else:
                                self.accountStatus = AccountStatus.NotSelected

            return self.ShowSelectAccount(self.accountStatus)

    def SeeAccount(self):
        print("[STEP4] See Balance/Deposit/Withdraw")
        if self.cardStatus == CardStatus.NotInserted:
            self.pinStatus = PinStatus.Incorrect
            self.accountStatus == AccountStatus.NotSelected
            return self.ShowCardStatus(self.cardStatus)
        elif self.pinStatus == PinStatus.Incorrect:
            self.accountStatus == AccountStatus.NotSelected
            return self.ShowPinStatus(self.pinStatus)
        elif self.accountStatus == AccountStatus.NotSelected:
            return self.ShowSelectAccount(self.accountStatus)
        else:
            b, d, w = self.account.GetInfo()
            print("***************************************")
            print("* Your Account {%s} Information *" %(self.account.name))
            print("* Balance : %d dollar(s)" %(b))
            print("* Deposit : %d dollar(s)" %(d))
            print("* Withdraw : %d dollar(s)" %(w))
            print("***************************************")
            return b, d, w

    def ShowCardStatus(self, status):
        if status == CardStatus.NotInserted:
            return " => Please, Insert Card."
        elif status == CardStatus.Inserted:
            return " => Card Detected, Please Input the pincode."

    def ShowPinStatus(self, status):
        if status == PinStatus.Incorrect:
            return " => Invalid Pincode, Try Again."
        elif status == PinStatus.Correct:
            return " => Valid Pincode, Select Account Please."

    def ShowSelectAccount(self, status):
        if status == AccountStatus.NotSelected:
            return " => Wrong Account Number, Check your Account again."
        elif status == AccountStatus.Selected:
            return " => Okay. You can see your account now"
