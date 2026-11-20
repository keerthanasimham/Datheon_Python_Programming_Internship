import re

responses = {
    "greeting": "Hello! Welcome to our assistant. How can I help you?",
    "hours": "Our business hours are Monday to Saturday, 9 AM to 6 PM.",
    "price": "Our products are available at affordable prices.",
    "products": "We offer different products. Please contact our support team for details.",
    "contact": "You can contact our support team through email.",
    "thanks": "You're welcome! Happy to help.",
}

def chatbot():
    print("===== WELCOME TO CHATBOT =====")
    print("Type 'bye', 'exit', or 'quit' to close the chatbot.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        if re.search(r"\b(bye|exit|quit)\b", user_input):
            print("Bot: Goodbye! Have a nice day.")
            break

        if re.search(r"\b(hello|hi|hey)\b", user_input):
            print("Bot:", responses["greeting"])

        elif re.search(r"\b(hours|timing|open|close)\b", user_input):
            print("Bot:", responses["hours"])

        elif re.search(r"\b(price|cost|payment)\b", user_input):
            print("Bot:", responses["price"])

        elif re.search(r"\b(product|products|items)\b", user_input):
            print("Bot:", responses["products"])

        elif re.search(r"\b(contact|email|support)\b", user_input):
            print("Bot:", responses["contact"])

        elif re.search(r"\b(thanks|thank you)\b", user_input):
            print("Bot:", responses["thanks"])

        else:
            print("Bot: Sorry, I didn't understand. Could you ask another question?")

chatbot()