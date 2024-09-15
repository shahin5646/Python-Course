""" How to find the difference between two numbers in Python """

fnum = int(input("Enter a Number: "))
lnum = int(input("Enter second Number: "))

def diff():
    if fnum > lnum:
        print('First Number is the biggest and difference is :  ',fnum-lnum)
        
    elif lnum>fnum:
        print("Last name is the biggest and difference is : ",lnum-fnum)
        
    else:
        print("Enter  a Valid Input>>>>>>>>>>!!!!!!!!!!")

diff()