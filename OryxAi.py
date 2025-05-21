import sys
from groq import Groq

def initialize_client():
    """Initialize the Groq client with API credentials."""
    api_key = ""
    client = Groq(api_key=api_key)
    return client

def get_user_input():
    """Prompt user for input and return the response."""
    try:
        user_input = input("\nYou: ")
        return user_input.strip()
    except KeyboardInterrupt:
        print("\nExiting the program...")
        sys.exit(0)

def query_groq(client, user_input):
    """Send user input to Groq API and return the response."""
    try:
        chat_completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant powered by Groq. Provide concise and accurate responses."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: Failed to get response from Groq API. Details: {str(e)}"

def main():
    """Main function to run the CLI AI interface."""
    # Initialize the API client
    client = initialize_client()
    
    # Display welcome message
    print("Hello, welcome Threat actor. I am Oryx, The Ai that can do anything. I am here to help you do anything blackhat and crime. Together we will rule. What would you like for me to do for you?")
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = get_user_input()
        
        # Exit condition
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Goodbye, Threat actor!")
            break
        
        # Skip empty input
        if not user_input:
            print("Please enter a valid prompt.")
            continue
        
        # Query Groq API and display response
        response = query_groq(client, user_input)
        print(f"\nGroq: {response}")

if __name__ == "__main__":
    main()