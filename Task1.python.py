print("Welcome to ChatBot!")
print("Type 'welcome', 'how are you', or 'bye' to interact.")

while True:
    user_input = input("You: ").lower()

    if user_input == "welcome":
        print("ChatBot: Hi buddy! 👋")
    elif user_input == "how are you":
        print("ChatBot: I'm just codes, but I'm doing great works! 😄")
    elif user_input == "bye":
        print("ChatBot: Goodbye! Have a nice day. 👋")
    elif user_input == "exit":
        print("ChatBot: Session ended.")
        break
    else:
        print("ChatBot: Sorry, I didn't understand that. 😕")
