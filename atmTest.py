from atmController import *
import sys

def TestCase1():
    # Test 1 : Normal Case
    print("Test 1 : Normal Case")

    atm = AtmController()

    # Step 1 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)

    # Step 3-1 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-2 : Select other Account
    ret = atm.SelectAccount("111-2222")
    print(ret)

    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-3 : Select another Account
    ret = atm.SelectAccount("333-4444")
    print(ret)

    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)


def TestCase2():
    # Test 2 : Card Insert Case
    print("Test 2 : Card Insert Case")

    atm = AtmController()

    # Step 1-1 : Reject Card
    ret = atm.InsertCard("REJECT")
    print(ret)

    # Step 1-2 : Wrong Command
    ret = atm.InsertCard("WRONG")
    print(ret)

    # Step 1-3 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)

    # Step 3 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)


def TestCase3():
    # Test 3 : Pinnumber Case
    print("Test 3 : Pinnumber Case")

    atm = AtmController()

    # Step 1 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 2-1 : PIN Number
    #ret = atm.PINnumber("1234")
    #print(ret)
    # Step 3 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 2-2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)
    # Step 3 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

def TestCase4():
    # Test 4 : Account Case
    print("Test 4 : Account Case")

    atm = AtmController()

    # Step 1 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)

    # Step 3-1 : Typing wrong account : Left side (no digit)
    ret = atm.SelectAccount("13m-3232")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-2 : Typing wrong account : Right side (no digit)
    ret = atm.SelectAccount("133-k235")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-3 : Typing wrong account : Right side last word (no digit)
    ret = atm.SelectAccount("133-723g")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-4 : Typing wrong account : Not in list
    ret = atm.SelectAccount("133-7235")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-5 : Select Right Account
    ret = atm.SelectAccount("123-4567")
    print(ret)
    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)


def TestCase5():
    # Test 5 : Step Flow Case
    print("Test 5 : Step Flow Case")

    atm = AtmController()

    # Step 1 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)

    # Step 3 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 1-1 : Reject Card
    ret = atm.InsertCard("REJECT")
    print(ret)
    # Step 4 : See Account => Can't see
    ret = atm.SeeAccount()
    print(ret)

    # Step 3-1 : Select Account => Start again from Step 1
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 1-2 : Insert Card
    ret = atm.InsertCard("INSERT")
    print(ret)

    # Step 3-2 : Select Account => Do also step 2 again
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 2 : PIN Number
    ret = atm.PINnumber("1234")
    print(ret)

    # Step 3-3 : Select Account
    ret = atm.SelectAccount("123-4567")
    print(ret)

    # Step 4 : See Account
    ret = atm.SeeAccount()
    print(ret)


testcase = sys.argv[1]

if testcase == '1':
    TestCase1()
elif testcase == '2':
    TestCase2()
elif testcase == '3':
    TestCase3()
elif testcase == '4':
    TestCase4()
elif testcase == '5':
    TestCase5()
else:
    print("Please choose (1~5)")
