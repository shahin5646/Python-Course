""" 
Suppose, you have to construct a list of string as following:
Name = Shikha,
Father Name = Muzam,
Mother Name = Haua,
Phone Number 01971700130

Construct a list using your Own Name, Father name, Mother name, Phone number. Write a program
to count the number of characters and count vowels from the list of strings you construct.

Sample Input:
[Shikhm Haua, Muzam, 01971700130]
Sample Output
Number of Character: 26
Number of Vowel: 7

Please justi
r answer line
line.
"""


# Construct the list
details = ['Shikha', 'Muzam', 'Haua', '01971700130']

# Combine the strings into a single string
combined_string = ' '.join(details)

# Count the number of characters
num_characters = len(combined_string)

# Function to count vowels
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Count the number of vowels
num_vowels = count_vowels(combined_string)

# Print the results
print("Number of Characters:", num_characters)
print("Number of Vowels:", num_vowels)
