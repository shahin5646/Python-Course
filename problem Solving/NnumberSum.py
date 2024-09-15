# Sum of numbers and average

number = int(input("How many number's sum: "))
total = 0

for i in range(number):
    num = int(input("Enter number: "))
    total+=num

average = total/number
print(average)