import time
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_banner():
    banner = """
     
 _______ _________ _______ _________
(  ____ \\__   __/(  ____ )\__   __/
| (    \/   ) (   | (    )|   ) (   
| (_____    | |   | (____)|   | |   
(_____  )   | |   |     __)   | |   
      ) |   | |   | (\ (      | |   
/\____) |___) (___| ) \ \_____) (___
\_______)\_______/|/   \__/\_______/
                                    
    """
    colors = {
        "A": "\033[91m",
        "B": "\033[92m",
        "C": "\033[93m",
        "D": "\033[94m",
        "E": "\033[95m",
        "F": "\033[96m",
        "G": "\033[97m",
        "R": "\033[0m",
    }
    for char in banner:
        if char in colors:
            print(colors[char] + char, end="")
        else:
            print(char, end="")
    print()

def starting_animation():
    print("\033[92mInitializing...\033[0m")
    time.sleep(1)
    print("\033[93mLoading...\033[0m")
    time.sleep(1)
    print("\033[95mReady!\033[0m")
    time.sleep(1)

def siri_chatbot():
    print("Hello! I am Siri, your friendly chatbot.")
    print("You can start chatting with me. Type 'exit' to end the chat.")
    while True:
        user_input = input("\033[96mYou: \033[0m")
        if user_input.lower() == "exit":
            break
        response = "Siri: I'm just a simple chatbot. I can't provide real answers, but I'm here to chat with you!"
        print("\033[95m" + response + "\033[0m")

if __name__ == "__main__":
    clear_screen()
    display_banner()
    starting_animation()
    siri_chatbot()
