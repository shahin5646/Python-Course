# factorial of a number

number = int (input("Enter A number: "))

def fact(n):
    if n==1:
        return n
    else :
        return n*fact(n-1)

result =fact(number)

print("Factorial is : ",result)    