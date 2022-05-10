#bomb party 2P: give a prompt and get a word from an implemented dictionary, request for a prompt loops infinitely unless the user terminates
import random
exit = False
word_list = []
#initializing a differently shuffeled word list at the start of every game
def initialize():
    with open('dict.txt') as f:
        for line in f:
            word_list.append(line)
    return None

def game_loop(mode):
    prompt = str(input("Give the current prompt:")).upper()
    if prompt == "TERMINATE":
        return 0
    
    if mode == "SHORT":
        solution = "how would you react if you saw a donkey eating your figs lmao"
        for word in word_list: 
            if (prompt in word and len(word) < len(solution)): solution = word
        if solution == "how would you react if you saw a donkey eating your figs lmao": solution = "NO AVAILABLE WORDS LOL!"
        else: 
            number = str(word_list.index(word))
            word_list.remove(word)
            print("SOLUTION: " + solution + "Index:" + number)
    
    elif mode == "LONG":
        solution = ""
        for word in word_list: 
            if (prompt in word and len(word) > len(solution)): solution = word
        if solution == "": solution = "NO AVAILABLE WORDS LOL!"
        else: word_list.remove(word)
    
    elif mode == "RAND" or mode == "ALFABET":
        solution = ""
        for word in word_list: 
            if prompt in word:
                solution = word
                break
        if solution == "": solution = "NO AVAILABLE WORDS LOL!"
        else: word_list.remove(word)
    
    elif mode == "BACK-ALFABET":
        solution = ""
        for index in range(len(word_list - 1), -1, -1): 
            if prompt in word_list[index]:
                solution = word_list[index]
                break
        if solution == "": solution = "NO AVAILABLE WORDS LOL!"
        else: word_list.remove(solution)
    
    
    
    
    print("SOLUTION: " + solution)
    return game_loop(mode)

def options_menu():
    while True:
        text = input("SELECT MODE: LONG/SHORT/RAND/ALFABET/BACK-ALFABET").upper()
        initialize()
        if text == "RAND" or text == "LONG" or text == "SHORT":
            random.shuffle(word_list)
        game_loop(text)
        return options_menu()

options_menu()