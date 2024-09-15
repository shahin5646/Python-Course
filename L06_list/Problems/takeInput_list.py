""" 
Write a Python program that takes a list as an input from the user. Then create a new
list excluding the first and last elements of the given list and prints the new list. If
there are not•enough elements in the list to do the task, the print "Not possible".
Sample Input:
Output: [3, 4, 5]
"""



def create_new_list(input_list):
    if len(input_list) < 3:
        print("Not possible")
    else:
        new_list = input_list[1:-1]
        print(new_list)

user_input = input("Enter a list of elements separated by spaces: ").split()
user_list = [int(x) for x in user_input]
create_new_list(user_list)
