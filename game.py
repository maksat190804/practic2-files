import random

def hangman():
    print('Добро пожаловать в игру Виселица')

    wordlist = ["мандарин", "яблоко", "груша", "виноград", "апельсин", "манго"]
    secret = random.choice(wordlist)
    quesses = "ауоыиэяюёе"
    turns = 5

    while turns > 0:
        missed = 0 
        for letter in secret:
            if letter in quesses:
                print(letter,end=' ')
            else:
                print(" ",end=" ")
                missed += 1
        if missed == 0:
            print("\n Ты выиграл!")
            break 
        quess = input("\n назови букву: ")
        quesses += quess

        if quess not in secret:
            turns -= 1
            print("\ Не угадал")
            print("\ Осталось попыток", turns)
            if turns < 5:print('\n | ')   
            if turns < 4:print(' o ')
            if turns < 3:print('/|\ ')    
            if turns < 2:print(' |  ')    
            if turns < 1:print('/ \ ')    
            if turns < 0: print("\n\n это слово: ", secret)      

ans = "да"
while ans == "да":
    hangman()
    print('хочешь сыграть снова? (да или нет)')
    ans = input()

        
