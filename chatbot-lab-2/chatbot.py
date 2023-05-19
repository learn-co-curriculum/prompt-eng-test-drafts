import openai
import time

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define a function to interact with the chatbot
def chat_with_chatbot(message):
    response = openai.Completion.create(
        engine='davinci',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15,
    )
    if response['choices']:
        return response['choices'][0]['text'].strip()
    else:
        return ""

# Main function to run the chatbot
def main():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Enter 'exit' to end the conversation.")

    # Initial prompt to start the conversation
    prompt = "You: Hi, how can I assist you today?\nChatbot:"

    while True:
        user_input = input(prompt)

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        prompt += ' ' + user_input.strip() + '\nChatbot:'
        response = chat_with_chatbot(prompt)

        if response:
            print(response)
            prompt += ' ' + response + '\nChatbot:'
        else:
            print("Chatbot: Sorry, I couldn't generate a response. Can you please rephrase or provide more information?")

        time.sleep(1)  # Delay for smoother conversation flow

if __name__ == '__main__':
    main()