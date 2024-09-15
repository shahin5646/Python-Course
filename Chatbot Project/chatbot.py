import json
from difflib import get_close_matches

class ChatBot:
    def __init__(self, knowledge_base_file="knowledge_base.json"):
        self.knowledge_base_file = knowledge_base_file
        self.load_knowledge_base()

    def load_knowledge_base(self):
        try:
            with open(self.knowledge_base_file, "r") as file:
                self.knowledge_base = json.load(file)
        except FileNotFoundError:
            self.knowledge_base = {"questions": []}

    def save_knowledge_base(self):
        with open(self.knowledge_base_file, "w") as file:
            json.dump(self.knowledge_base, file, indent=2)

    def find_best_match(self, user_question:str, questions:list[str])->str|None:
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def get_answer_for_question(self, question:str)->str|None:
        for q in self.knowledge_base["questions"]:
            if q["question"] == question:
                return q["answer"]
        return None

    def chat(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break

            best_match = self.find_best_match(user_input, [q["question"] for q in self.knowledge_base["questions"]])

            if best_match:
                answer = self.get_answer_for_question(best_match)
                print(f"Mr.Robot: {answer}")
            else:
                print("Mr.Robot: I don't know the answer. Can you teach me?")
                new_answer = input('Type the answer or "skip" to skip:  ')
                if new_answer.lower() != "skip":
                    self.knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    self.save_knowledge_base()
                    print("Mr.Robot: Thank you, I learned a new response!")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat()
    
