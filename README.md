# ATMcontroller


## Introduction

* This program is a test project for checking personal coding skill. It's not a commercial program.

AMTcontroller is a virtual banking class for checking card insertion, pincode and choosing account and getting balance, deposit and withdraw.

The Process follows below steps.

```bash
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
```

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

+------------+--------------------------------------------+
| Ctrl + u   | Load all of the images from a directory    |
+------------+--------------------------------------------+
| Ctrl + r   | Change the default annotation target dir   |
+------------+--------------------------------------------+

+---+----------------+--------------------------+
|Num| Name           |Input                     |
+---+----------------+--------------------------+
| 1 | InsertCard     |string belows.            |
|   |                |"REJECT", "INSERT"        |
+---+----------------+--------------------------+
| 2 | PINnumber      | 4 digit string.          |
|   |                | ex) "1234"               |
+---+----------------+--------------------------+
| 3 | SelectAccount  |8 string.                 |
|   |                |ex) "123-4567"            |
+---+----------------+--------------------------+
| 4 | SeeAccount     |None                      |
+---+----------------+--------------------------+



