""" 
Consider the following random items code of groceries.

d=181,178,187,182,192,189,202,201

The concept of dataset is crucial for modern intelligence systems. Initially, we need to process any data using basic programming concepts such as statistical analysis. Here providing data is also part of that concept which is provided in your class lecture.

a)Create a list constructor for the provided dataset.
b)Develop a function for the data where the function will regenerate the values in reverse and sorted way following all the necessary requirements.


"""



# d=181,178,187,182,192,189,202,201


list_01=list([181,178,187,182,192,189,202,201])
print(type(list_01))

def sorting():
    list_01.sort(reverse=True)
    print('Reverse List: ',list_01)
    
    list_01.sort()
    print('Sorted List: ',list_01)

sorting()