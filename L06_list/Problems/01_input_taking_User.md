Sure, here's the information formatted as a Markdown document with sample outputs:

```markdown
# Input Methods for Lists, Tuples, Dictionaries, and Sets in Python

## Lists:

1. **Using `input()` with `split()`:**
   ```python
   user_input = input("Enter elements separated by spaces: ")
   my_list = user_input.split()
   ```

   Sample Output:
   ```
   Enter elements separated by spaces: 1 2 3 4 5
   my_list = ['1', '2', '3', '4', '5']
   ```

2. **Using list comprehension:**
   ```python
   user_input = [int(x) for x in input("Enter elements separated by spaces: ").split()]
   ```

   Sample Output:
   ```
   Enter elements separated by spaces: 1 2 3 4 5
   my_list = [1, 2, 3, 4, 5]
   ```

3. **Using a loop:**
   ```python
   my_list = []
   n = int(input("Enter number of elements: "))
   for _ in range(n):
       my_list.append(input("Enter element: "))
   ```

   Sample Output:
   ```
   Enter number of elements: 3
   Enter element: a
   Enter element: b
   Enter element: c
   my_list = ['a', 'b', 'c']
   ```

## Tuples:

1. **Using `input()` with `split()`:**
   ```python
   user_input = input("Enter elements separated by spaces: ")
   my_tuple = tuple(user_input.split())
   ```

   Sample Output:
   ```
   Enter elements separated by spaces: 1 2 3 4 5
   my_tuple = ('1', '2', '3', '4', '5')
   ```

2. **Using tuple comprehension:**
   ```python
   user_input = [int(x) for x in input("Enter elements separated by spaces: ").split()]
   my_tuple = tuple(user_input)
   ```

   Sample Output:
   ```
   Enter elements separated by spaces: 1 2 3 4 5
   my_tuple = (1, 2, 3, 4, 5)
   ```

## Dictionaries:

1. **Using a loop:**
   ```python
   my_dict = {}
   n = int(input("Enter number of key-value pairs: "))
   for _ in range(n):
       key = input("Enter key: ")
       value = input("Enter value: ")
       my_dict[key] = value
   ```

   Sample Output:
   ```
   Enter number of key-value pairs: 2
   Enter key: name
   Enter value: John
   Enter key: age
   Enter value: 30
   my_dict = {'name': 'John', 'age': '30'}
   ```

2. **Using dictionary comprehension:**
   ```python
   n = int(input("Enter number of key-value pairs: "))
   my_dict = {input("Enter key: "): input("Enter value: ") for _ in range(n)}
   ```

   Sample Output:
   ```
   Enter number of key-value pairs: 2
   Enter key: name
   Enter value: John
   Enter key: age
   Enter value: 30
   my_dict = {'name': 'John', 'age': '30'}
   ```

## Sets:

1. **Using `input()` with `split()`:**
   ```python
   user_input = input("Enter elements separated by spaces: ")
   my_set = set(user_input.split())
   ```

   Sample Output:
   ```
   Enter elements separated by spaces: 1 2 3 4 5
   my_set = {'1', '2', '3', '4', '5'}
   ```

2. **Using a loop:**
   ```python
   my_set = set()
   n = int(input("Enter number of elements: "))
   for _ in range(n):
       my_set.add(input("Enter element: "))
   ```

   Sample Output:
   ```
   Enter number of elements: 3
   Enter element: a
   Enter element: b
   Enter element: c
   my_set = {'a', 'b', 'c'}
   ```

3. **Using set comprehension:**
   ```python
   n = int(input("Enter number of elements: "))
   my_set = {input("Enter element: ") for _ in range(n)}
   ```

   Sample Output:
   ```
   Enter number of elements: 3
   Enter element: a
   Enter element: b
   Enter element: c
   my_set = {'a', 'b', 'c'}
   ```

Choose the appropriate input method based on your requirements and preferences.
```

