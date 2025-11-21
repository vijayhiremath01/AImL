import requests
 #its like a norrowing library book - requests is a free tools to talk to websites like (sending or recienving data over internet )
# without ir no , AI chat bots , web scrapping , API interaction would be possible

from colorama import Fore , Style , init 
init(autoreset = True)
#magic colorufull text in terminal 
#fore - foreground color , Style - text style , init - to initialize colorama   

import os 
#python built in library to interact with operating system like folders and files and all 

from dotenv import load_dotenv 
#tiny library to load and keep safe the secret keys and enviromental variables from .env file
#load_dotenv() = "Hey read the .env file and load all the secret keys and enviromental variables from there"

import sys 
#importing the main boss system library to interact with the python runtime environment

# NOTE : order matters load secrets earlier before using them  

# Load environment variables from .env file
load_dotenv()

# Get API_KEY from environment variables
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print(Fore.RED + "Error: API_KEY not found in environment variables.")
    sys.exit(1)


# IMPORTANT QUESTIONS / ANSWERS 
# 1 . "What's os.getenv for, and why not hardcode secrets?" (Ans: Env vars for security/config; hardcode risks exposure in repos.)
# 2 . "Explain from X import Y vs import X." (Ans: Specific pulls only needed bits—faster, cleaner namespace; general imports whole module.)
# 3 . "How'd you handle missing .env?" (Ans: Check if not API_KEY: print('Error'); exit()—defensive.)

# Working model
MODEL_NAME = "llama-3.1-8b-instruct"  # Note: Your code has "instant"—both work, instruct=better for chats

#Interview Qs:
# "Why use constants like MODEL_NAME?" (Ans: Readability, easy global swaps—no hunting.)
# "Tradeoffs of 8B vs 70B models?" (Ans: 8B=cheap/fast, 70B=accurate but $$$slower —depends on use case.)

headers = {  # Line 21
        "Authorization": f"Bearer {API_KEY}",  # Line 22
        "Content-Type": "application/json",  # Line 23
        "Accept": "application/json",  # Line 24
    }  # Line 25

# Example chat history; replace with your actual conversation history as needed
history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

data = {  # Line 28
        "model": MODEL_NAME,  # Line 29
        "messages": history,  # Line 30
        "temperature": 0.7,  # Line 31
    }  # Line 32

#Tells AI "what/ how"—vague data = dumb replies. Real life: Google search "data" = your query; tune temp low for code gen, high for stories.

#interview Qs: "Temperature role?" (Balances creativity vs reliability—0.2 for math, 0.8 for brainstorming.) | "History overflow fix?" (Slice: history[-10:]—keeps last 10, saves cash/tokens.)

try: 
    response = requests.post(API_KEY, headers=headers, json=data, timeout=10)
    #Interview Qs: "Timeout why?" (Prevents hangs—user UX killer; set per app speed.) | "Sync vs async requests?" (Sync simple; async scales—use aiohttp for pro bots.)
    if response.status_code == 401:  # Line 38
        print(Fore.RED + "❌ Invalid API Key. Update API_KEY in .env")  # Line 39
        sys.exit(1)  # Line 40
    if response.status_code != 200:  # Line 44
        print(Fore.RED + "❌ Groq API ERROR:", response.status_code)  # Line 45
        print(response.text[:300])  # Line 46
        sys.exit(1)  # Line 47
        result = response.json()  # Line 50
        reply_text = result["choices"][0]["message"]["content"]  # Line 51
        print(Fore.GREEN + "AI Reply:", reply_text)  # Line 52

except Exception as e:  # Line 53
        print(Fore.RED + "❌ Server Hang / No Response:", str(e))  # Line 54
        sys.exit(1)  # Line 55       