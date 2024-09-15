"""
Question:
You are given a list of 7 days in 1 a week sequentially starting from Saturday. Monday and Wednesday  are missing from the list. So, write a python code to add the missing items in the list. In addition, create a function which will take the day from the list and give a message "Today is holiday" if it matches with "Friday" otherwise it will show "Working day".

 """
weekdays = ['saturday', 'sunday', 'tuesday', 'thursday', 'friday']

# Insert missing days
weekdays.insert(2, 'monday')
weekdays.insert(4, 'wednesday')

print(weekdays)

def check_days(day):
    day = day.lower()  
    if day in weekdays:
        if day == 'friday':
            print('Today is holiday')
        else:
            print('Working day')
    else:
        print('Invalid day')

day_input = input('Enter the Day (small letters): ')
check_days(day_input)
