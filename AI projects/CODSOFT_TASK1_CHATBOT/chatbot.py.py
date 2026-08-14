from datetime import datetime

print("=" * 50)
print("🤖 Welcome to My AI Chatbot")
print("=" * 50)
print("Type 'help' to see what I can answer.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey", "hii"]:
        print("Bot: Hello! 👋 How can I help you?")

    # Name / identity
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a rule-based AI chatbot created for the CODSOFT internship.")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! 😊 Thanks for asking.")

    # AI
    elif "what is ai" in user_input or "artificial intelligence" in user_input:
        print("Bot: Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.")

    # Programming
    elif "programming" in user_input or "coding" in user_input:
        print("Bot: Programming is the process of creating instructions that computers can execute.")

    # Python
    elif "python" in user_input:
        print("Bot: Python is a popular programming language used in AI, machine learning, web development, and data science.")

    # Capabilities
    elif "what can you do" in user_input or "help" in user_input:
        print("Bot: I can answer basic questions about AI, programming, Python, and general conversation.")

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Date
    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}.")

    # Thanks
    elif "thanks" in user_input:
        print("Bot: You're welcome! 😊")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Please try asking something else.")