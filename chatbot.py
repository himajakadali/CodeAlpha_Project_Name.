import nltk
from nltk.chat.util import Chat, reflections

# Download necessary resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ['I am a chatbot created by you.']),
    (r'how are you?', ['I am just a program, but I am doing fine.']),
    (r'quit', ['Bye!', 'Goodbye!', 'See you later!']),
    (r'(.*)', ['I am not sure how to respond to that.'])
]

def create_chatbot():
    chatbot = Chat(pairs, reflections)
    return chatbot

def chat():
    chatbot = create_chatbot()
    print("Hello! I am a chatbot. Type 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat()
