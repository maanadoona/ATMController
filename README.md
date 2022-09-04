# ATMcontroller
* This program is a test project for checking personal coding skill. It's not a commercial program.

## Introduction

* AMTcontroller is a virtual banking class for checking card insertion, pincode and choosing account and getting balance, deposit and withdraw.

* The Process follows below steps.

```bash
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
```
** If Card is rejected, You need to start from step 1 again.


#### Step 1) Insert Card
At first, You need to call the function of ```InsertCard``` with status value 'insert or not' when the card is inserted or rejected.

#### Step 2) PIN number
Next, You call the function of ```PINnumber``` with pinnumber value that is composed of 4-digit.
AMTcontroller checks pinnumber is right. If pinnumber is right, then you will get the account list.

#### Step 3) Select Account
You select the one of Account list. You call the function of ```SelectAccount``` with account you selected.
If you send right account name, you can go to step 4.

#### Step 4) See Balance/Deposit/Withdraw
You just call the function of '''SeeAccount'''. You will get the Balance/Deposit/Withdraw

## API Usage

| Num | Name | Input |Output|
|:----:|:------------|:------------------------|:------------------------|
|1     |InsertCard   |string belows.           |"INSERT" : "Card Detected, Please Input the pincode."
|      |             |"REJECT", "INSERT"       |"REJECT" : "Please, Insert Card."
|2     |PINnumber    |4 digit string.          | Valid : "Valid Pincode, Select Account Please."
|      |             |ex) "1234"               | Invalid : "Invalid Pincode, Try Again."
|3     |SelectAccount|8 string.                | Valid : list of accounts. ex) ["123-4567", "111-2222", "333-4444"]
|      |             |ex) "123-4567"           | Invalid : "Wrong Account Number, Check your Account again."
|4     |SeeAccount   |None                     | Three values. (Balance, Deposit, Withdraw) ex) (700, 1000, 300)



## Test Case

#### Test 1 : Normal Case

 This is test for normal case. All steps are right things.



#### Test 2 : Card Insert Case

 Card Insert Parameter has three things. "INSERT", "REJECT" and Other all characters(Wrong commands).



#### Test 3 : Pin number Case

 Pin number has 4-digit value.  Wrong pin number or Skip of this step makes error. 



#### Test 4 : Account Case

 After two steps, you get the account list. If you send wrong account number, you can't get the account information. 



#### Test 5 : Step Flow Case

If card is rejected at any step, It will go back to step 1 (Card Insert Check). You need to start again from step 1.



##  How to run

```bash
python atmTest.py [number(1~5)]

ex) python atmTest.py 1
```



