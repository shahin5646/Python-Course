""" 
Define two lists and write a python program that print a new list elements of those lists otherwise print no common elements. 

Sample Input: First List [1, 2, 3] and Second List [2, 4, 5] 

Output: [2]

"""


first_list = [1, 28, 3]
second_list = [2, 4, 5]

# Initialize an empty list to store common elements
common_elements = []

for element in first_list:
   
    if element in second_list:
        common_elements.append(element)
        
        
        


# Check if there are any common elements
if common_elements:
    print(common_elements)
else:
    # If there are none, print a message indicating no common elements
    print("No common elements")
