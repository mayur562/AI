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


# Main Program
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
