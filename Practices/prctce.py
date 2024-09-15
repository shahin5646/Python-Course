import random
import sys

from enum import Enum
class diu_student(Enum):
    NABIL =5350
    FaRUK =5874
    SHAHIN  =5646



student_Choice =input('Enter :\n5350 for Nabil\n5874 for Faruk\n5646 for SHAHIN\n')
student =int(student_Choice)

choice=['5350','5646','5874']
diu_random =random.choice(choice)
diu_chooice =int(diu_random)

if student<5350 or student>5874:
    sys.exit('You must Type any Valid Id')
    

print('You Type:'+str(diu_student(student)).replace('diu_student.',' '))
print('daffodil Choose:'+str(diu_student(diu_chooice)).replace('diu_student.',' '))



if student==5350 and diu_chooice ==5646:
    print("Daffodil selected Nabil👦")
elif student==5874 and diu_chooice ==5350:
    print("Daffodil selected Faruk👩‍🦲")
elif student==5646 and diu_chooice ==5874:
    print("Daffodil selected SHAHIN🙆‍♂️")
elif student==diu_chooice:
    print('Kopaaaaaal Pura☠️')
else:
    print('Nobody is Selected😁')