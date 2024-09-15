# Answer Number 2B

"""
How can you write a Python program to calculate the total and payable cost of books based on the number of books purchased, applying a discount if applicable?

Example Input and Output:
Enter the number of books: 5
Price of book-1: 100
Price of book-2: 150
Price of book-3: 200
Price of book-4: 250
Price of book-5: 300

Sample Output
Total Cost: 1000tk
Total Payable Cost: 900.0tk (10% discount applied for purchasing 5 books) """


def calculate_total_cost(num_books, book_prices):
    total_cost = sum(book_prices)
    
    if num_books >= 4 and num_books <= 10:
        discount = 0.1
    elif num_books > 10:
        discount = 0.2
    else:
        discount = 0
    
    total_payable_cost = total_cost - (total_cost * discount)
    return total_cost, total_payable_cost, discount

def main():
    num_books = int(input("Enter the number of books: "))
    book_prices = []
    for i in range(1, num_books + 1):
        price = float(input(f"Price of book-{i}: "))
        book_prices.append(price)
    
    total_cost, total_payable_cost, discount = calculate_total_cost(num_books, book_prices)
    
    print("\nSample Output")
    print(f"Total Cost: {total_cost}tk")
    if discount > 0:
        print(f"Total Payable Cost: {total_payable_cost}tk ({int(discount*100)}% discount applied for purchasing {num_books} books)")
    else:
        print("No discount applied for purchasing less than 4 books")


main()
