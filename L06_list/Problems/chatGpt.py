""" 
Consider the following scenario for the Chatgpt

You: Hi!

Chatgpt: Hi! What can I do now?

You: Do you know me?

Chatgpt: You are from Daffodil Intern semester. Rubayat ional University. You are currently studying 5th senester.

You: Thanks for your information.

Chatgpt: Thanks for your gratitude.

You know that chatgpt is a complex artificial system. And it requires a more powerful system such as a supercomputer. You have no development knowledge of a chatgpt but you have the basic knowledge of object oriented programming II. Now you need to implement some concepts to develop the demo chatgpt.

a)Construct a function to build the demo Chatgpt and all necessary input will take form the user as their wishes.

b) Justify the line from your demo chatgpt "Chatgpt is better than human".

c) Explain the process to change the word "5th" to "7th" in the given string.


"""


def greeting():
    return "Hi! What can I do for you?"

def get_user_input():
    return input("You: ")

def respond(user_input):
    if "know me" in user_input:
        return "You are from Daffodil International University. You are currently studying in 5th semester."
    elif "Thanks" in user_input:
        return "Thanks for your gratitude."
    else:
        return "I'm not sure how to respond to that."

def main():
    print(greeting())
    
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            break
        response = respond(user_input)
        print(f"ChatGPT: {response}")


main()
