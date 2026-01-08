import datetime

BOT_NAME = "MITRA"

print(f"Namaste! 🙏 I am {BOT_NAME}, your friendly AI chatbot.")
print("I’m here to help you learn and stay motivated 😊")
print("Type 'help' to see what I can do, or 'bye' to exit.\n")

responses = {
    "hello": f"Hello! 👋 I’m {BOT_NAME}. How can I help you today?",
    "hi": f"Hi there! 😊 {BOT_NAME} at your service.",
    "hey": "Hey! Nice to see you 😄",
    "how are you": "I’m feeling awesome and ready to help 💪 How about you?",
    "who are you": f"I am {BOT_NAME}, a rule-based AI chatbot built using Python 🐍",
    "motivation": "Small steps every day lead to big success. Don’t stop! 🔥",
    "python": "Python is beginner-friendly and powerful. Great choice to learn! 🚀",
    "thanks": "You’re welcome! 😊 Happy to help.",
    "thank you": "Always here for you 🙌",
    "time": lambda: f"🕒 Current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "date": lambda: f"📅 Today’s date is {datetime.date.today()}",
    "help": (
        "You can ask me about:\n"
        "• Greetings (hello / hi)\n"
        "• Python\n"
        "• Motivation\n"
        "• Time / Date\n"
        "• Who I am\n"
        "• Type 'bye' to exit"
    ),
    "bye": "Goodbye! 👋 Keep learning and stay awesome 🌟",
    "exit": "See you soon! 👋",
    "quit": "Bye! Take care 😊"
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()

    # Check longer keys first (better matching)
    for key in sorted(responses, key=len, reverse=True):
        if key in user_input or key in words:
            value = responses[key]
            return value() if callable(value) else value

    return "Hmm 🤔 I didn’t get that yet. Try typing **help**."

# Main loop
while True:
    user_input = input("You: ")
    reply = get_response(user_input)
    print(f"{BOT_NAME}: {reply}")

    if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
        break
