import random
from colorama import Fore, Style

word_list = []
def initialize():
    with open('dict.txt') as f:
        for line in f:
            word_list.append(line)
    return None

def game_loop(mode):
    prompt = str(input("Give the current prompt: ")).upper()
    if prompt == "TERMINATE":
        return 0
    if mode == "SHORT":
        solution = "how would you react if you saw a donkey eating your figs lmao"
        for word in word_list: 
            if (prompt in word and len(word) < len(solution)): solution = word
        if solution == "how would you react if you saw a donkey eating your figs lmao": print("NO AVAILABLE WORDS LOL!")
        else: 
            word_list.remove(word)
            print(Fore.GREEN + "SOLUTION: " + Fore.RED + solution + Style.RESET_ALL)
    elif mode == "LONG":
        solution = ""
        for word in word_list: 
            if (prompt in word and len(word) > len(solution)): solution = word
        if solution == "": print("NO AVAILABLE WORDS LOL!" + "")
        else: 
            word_list.remove(word)
            print(Fore.GREEN + "SOLUTION: " + Fore.RED + solution + Style.RESET_ALL)
    elif mode == "RAND" or mode == "ALFABET":
        solution = ""
        for word in word_list: 
            if prompt in word:
                solution = word
                break
        if solution == "": print("NO AVAILABLE WORDS LOL!" + "")
        else: 
            number = str(word_list.index(word))
            word_list.remove(word)
            print(Fore.GREEN + "SOLUTION: " + Fore.RED + solution + Fore.GREEN + "Index:    " + Fore.RED + number + Style.RESET_ALL)
    elif mode == "BACK-ALFABET":
        solution = ""
        for index in range(len(word_list) - 1, -1, -1): 
            if prompt in word_list[index]:
                solution = word_list[index]
                break
        if solution == "": print("NO AVAILABLE WORDS LOL!" + "")
        else: 
            number = str(len(word_list)-(word_list.index(solution) + 1))
            word_list.remove(solution)
            print(Fore.GREEN + "SOLUTION: " + Fore.RED + solution + Fore.GREEN + "Index:    " + Fore.RED + number + Style.RESET_ALL)
    return game_loop(mode)

def options_menu():
    while True:
        text = input("SELECT MODE LONG/SHORT/RAND/ALFABET/BACK-ALFABET/EXIT: ").upper()
        initialize()
        if text == "RAND" or text == "LONG" or text == "SHORT":
            random.shuffle(word_list)
        if text == "EXIT":
            return
        game_loop(text)
        
options_menu()