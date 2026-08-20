def rule_based_bot(user_input):
    text = user_input.lower()
    if "hello" in text:
        return "Hi there! How can I help you today?"
    elif "hours" in text:
        return "We're open 9 AM to 6 PM, Mon–Fri."
    elif "bye" in text:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that."

while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        break
    print("Bot:", rule_based_bot(msg))
