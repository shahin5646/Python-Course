""" 
Daffodil International universlty has been dicided  to givee waiver to stusents
during pandemic according to the following criteria:
Result (CGPA)
More than 3.50 waiver is 20%
3.00-3.50 waiver is 10%
Less than 3.00 waiver is 5%

Take your semester fee and result as user input and print the net waiver amount.

"""

semester_fee =int(input('Enter Semester Fee: '))
CGPA =float(input('Enter CGPA:'))

if CGPA>3.50:
    print("Semester Fee is  ",(semester_fee - (semester_fee*0.2)))
elif 3.00<CGPA<=3.50 :
    print("Semester Fee is  ",(semester_fee - (semester_fee*0.1)))
elif CGPA<3.00:
    print("Semester Fee is  ",(semester_fee - (semester_fee*0.05)))
    

    