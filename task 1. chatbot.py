import re
def chatbot(user_input):
    user_input = user_input.lower()

    rules = {
        r'hello|hi|hey': 'Hello! Swapnil How can I help you?',
        r'how are you': 'I am a chatbot, so I don\'t have feelings, but thanks for asking!',
        r'your name|who are you': 'I am your chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'who am i': 'You are Swapnil Mane.My boss.',
        r'thank you|thanks': 'You\'re welcome!',
        r'weather': 'I\'m sorry, I don\'t have the capability to check the weather.',
        r'help': 'I can respond to basic queries. Try asking about my name, age, or just say hello!',
    }

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"

if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything or say goodbye to end the conversation.")

    for _ in range(10):
        user_input = input("User: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot(user_input)
            print(" Chatbot:", response)
