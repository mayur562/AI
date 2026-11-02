import re

def get_response(user):
    user = user.lower()

    if re.search(r"\b(hi|hello|hey)\b", user):
        return "Hello! Welcome to Customer Support."

    elif re.search(r"order|track|tracking", user):
        return "Please enter your Order ID to track your order."

    elif re.search(r"return|replace|exchange", user):
        return "Returns are accepted within 7 days."

    elif re.search(r"refund", user):
        return "Refunds take 5–7 business days."

    elif re.search(r"cancel", user):
        return "Orders can only be cancelled before shipping."

    elif re.search(r"payment", user):
        return "We accept UPI, Cards and COD."

    elif re.search(r"delivery|shipping", user):
        return "Delivery usually takes 3–5 business days."

    elif re.search(r"contact", user):
        return "Email: support@company.com"

    elif re.search(r"\b(bye|exit)\b", user):
        return "Thank you! Have a nice day."

    else:
        return "Sorry, I couldn't understand your question."


print("=" * 45)
print("        Customer Support Chatbot")
print("Type 'bye' or 'exit' to end the chat.")
print("=" * 45)

while True:
    user_input = input("\nYou: ")

    response = get_response(user_input)


    print("Bot:", response)

    if re.search(r"\b(bye|exit)\b", user_input.lower()):
        break































'''
Algorithm: Customer Support Chatbot using Regular Expressions

1. Start the program.
2. Import the re module to identify keywords and patterns in user messages.
3. Define a function get_response() that accepts the user's input.
4. Convert the user's message into lowercase to make keyword matching case-insensitive.
5. Check the user's message using regular expressions (re.search()) for the following keywords:
   a) If the message contains "hi", "hello", or "hey", display a welcome message.
   b) If it contains "order", "track", or "tracking", ask for the Order ID.
   c) If it contains "return", "replace", or "exchange", provide the return policy.
   d) If it contains "refund", display the refund processing time.
   e) If it contains "cancel", provide the order cancellation policy.
   f) If it contains "payment", display the accepted payment methods.
   g) If it contains "delivery" or "shipping", display the delivery time.
   h) If it contains "contact", display the customer support email.
   i) If it contains "bye" or "exit", display a goodbye message.
6. If no matching keyword is found, display a default message saying that the question is not understood.
7. Display the chatbot welcome message and instructions.
8. Start an infinite loop to continuously accept messages from the user.
9. Pass each user message to the get_response() function and display the chatbot's response.
10. If the user enters "bye" or "exit", terminate the loop and end the conversation.
11. Stop the program.

'''
