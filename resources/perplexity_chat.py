# THIS IS SAMPLE PERPLEXITY CODE TO WORK WITH PERPLEXITY API 
# Sent up venv: python3 -m venv venv
# Activate venv: source venv/bin/activate
# RUN: python perplexity_chat.py "Why is Grok 3 garnering so much attention right now?" 

# pip install requests


import sys
import requests

def main():
    # Replace <YOUR_API_KEY> with your actual Perplexity API key
    api_key = "<YOUR_API_KEY>" 
    
    # If the user didn’t provide a question as a command-line argument, prompt them
    if len(sys.argv) < 2:
        user_prompt = input("Enter your prompt: ")
    else:
        # Gather all command-line arguments into a single string
        user_prompt = " ".join(sys.argv[1:])
    
    # Perplexity API endpoint
    url = "https://api.perplexity.ai/chat/completions"
    
    # Customize the payload as needed
    payload = {
        "model": "sonar-pro",  # Choose an available model like sonar-reasoning or sonar-pro https://docs.perplexity.ai/guides/model-cards
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        # Optional parameters:
        "max_tokens": 256,
        "temperature": 0.2,
        "top_p": 0.9,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return
    
    # Print the raw JSON text or parse it as needed
    print("Raw API Response:")
    print(response.text)
    
    # If you want to parse and print only the assistant's text, do:
    try:
        response_json = response.json()
        # The text is typically found at response_json["choices"][0]["message"]["content"]
        answer = response_json["choices"][0]["message"]["content"]
        
        print("\nAssistant's Response:")
        print(answer)
    except (KeyError, IndexError, ValueError):
        print("Could not parse the response properly.")

if __name__ == "__main__":
    main()
