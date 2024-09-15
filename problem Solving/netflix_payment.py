""" 
Streaming pioneer Netflix significantly expanded its global footprint to 190 
countries, making its Internet TV service available in 130 new markets
including Bangladesh. The internet TV network expanded to more than 130
countries apart from China, Syria, Crimea or North Korea. The Netflix is a
popular streaming platform  in Bangladesh. OTT lovers can get Netflix offers
three streaming plans: Basic, Standard, and Premium, starting at  S9.99 per
month and ending at $19.99 month. Standard  pIan may cost S15.99.
Now your task is creating a nested dictionary by taking user input.
Example,dict — {1: {"namer: "Siri". "plan": "Basic"). 2: {"name"$fAIexa",
"plan": "Standard"))
Prepare a function which insert payment in nested dict base on their prefer
plan and print out the amount of the payment.
 """




def insert_payment(user_dict):
    for key, value in user_dict.items():
        plan = value["plan"]
        if plan == "Basic":
            user_dict[key]["payment"] = "$9.99"
        elif plan == "Standard":
            user_dict[key]["payment"] = "$15.99"
        elif plan == "Premium":
            user_dict[key]["payment"] = "$19.99"
        else:
            print("Invalid plan for user:", value["name"])

    # Print out the payment 
    for key, value in user_dict.items():
        print(f"Name: {value['name']}, Payment: {value.get('payment', 'Plan not found')}")

def main():
    num_users = int(input("Enter the number of users: "))
    user_dict = {}

    for i in range(1, num_users + 1):
        name = input(f"Enter name for user {i}: ")
        plan = input(f"Enter plan (Basic/Standard/Premium) for user {i}: ")
        user_dict[i] = {"name": name, "plan": plan}

    insert_payment(user_dict)

main()



""" 
Explanation:
- We define a function `insert_payment` to insert payment information into the nested dictionary based on the preferred plan.
- The function iterates through the dictionary, checks the plan for each user, and assigns the corresponding payment amount.
- We then print out the payment for each user.
- In the `main` function, we take user input for the number of users and their names and preferred plans.
- We create a nested dictionary to store this information.
- Finally, we call the `insert_payment` function to calculate and print the payment for each user.
 """