import time

shutdown = False
time_left = 0

def zero_time_left():
    global shutdown, time_left
    if time_left == 0:
        print('Time left until shutdown: 0')
        shutdown = True

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning perfectly! How about you?"
    elif "what's your age" in user_input:
        return "I'm a program that is constantly updated, so I am always new!"
    elif "help" in user_input:
        return "Sure! I can help you. What do you need?"
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

def main():
    global time_left, shutdown
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' or 'goodbye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Bye!")
            break

        # Get chatbot response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

        # Handle follow-up when user asked for help
        if response == "Sure! I can help you. What do you need?":
            user_input_help = input("You: ")
            if user_input_help.lower() == "call 911":
                print('Calling...')
                time.sleep(3)
                print("911, What's your emergency?")
            elif user_input_help.lower() == "emergency shutdown":
                print('Shutting down in 1 min')
                time_left = 60
                while time_left > 0 and not shutdown:
                    print('Time left until shutdown:', time_left)
                    time.sleep(1)
                    time_left -= 1
                    zero_time_left()
                if shutdown:
                    print("System has been shut down.")
                    break

if __name__ == "__main__":
    main()
