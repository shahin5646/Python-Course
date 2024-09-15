import json
from difflib import get_close_matches
import flet as ft

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Text(message.user_name, weight="bold"),
                        ft.Text(message.text, selectable=True, width=500),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

def load_knowledge_base(file_path:str)->dict:
    with open(file_path, "r") as file:
        data:dict = json.load(file)
    return data

def save_knowledge_base(file_path:str, data:dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question:str, questions:list[str])->str|None:
    matches:list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question:str, knowledge_base:dict)->str|None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:  
            return q["answer"]  
    return None  

def chatbot_response(user_input: str, knowledge_base: dict, file_path: str) -> str:
    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    if best_match:
        answer = get_answer_for_question(best_match, knowledge_base)
        return answer
    else:
        print("MediBot: I don't know the answer. Can you teach me?")
        new_answer = input('Type the answer or "skip" to skip:  ')
        if new_answer.lower() != "skip":
            knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            save_knowledge_base(file_path, knowledge_base)  # Save the updated knowledge base to the JSON file
            print("MediBot: Thank you, I learned a new response!")
            return new_answer
        else:
            return "I don't know the answer."

def main(page: ft.Page):
    page.title = "MediBot"
    page.theme_mode = "light"
    page.fonts = {
        
        "comic": "comic.ttf"
    }

    knowledge_base = load_knowledge_base("knowledge_base.json")

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "We need to know our names first!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.", message_type="login_message"))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(page.session.get("user_name"), new_message.value, message_type="chat_message"))
            page.pubsub.send_all(Message(user_name="MediBot", text="MediBot is getting the response for you...", message_type="login_message"))
            ai_response = chatbot_response(str(new_message.value), knowledge_base, "knowledge_base.json")
            page.pubsub.send_all(Message("MediBot", str(ai_response).lstrip(), message_type="chat_message"))
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    join_user_name = ft.TextField(
        label="Tell me your name Sir...",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome! I am MediBot. Your Digital Health Consultant. "),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Feel free to ask ,Sir...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=55,
        filled=True,
        expand=True,
        border_radius=20,
        on_submit=send_message_click,
        border_color=ft.colors.BLUE
    )

    page.add(
        ft.Row([ft.Text("MediBot", font_family="comic", style="headlineLarge", color="blue")], alignment="center"),
        ft.Container(
            content=chat,
            border=ft.border.all(2, ft.colors.BLUE),
            border_radius=20,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                    icon_color=ft.colors.BLUE
                ),
            ]
        ),
    )

ft.app(port=8550, target=main, view=ft.WEB_BROWSER, assets_dir="assets")
