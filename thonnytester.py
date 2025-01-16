from tkinter import *
import time
import json
import random

def start():
    global available_letters
    global guessed_letters
    global lives_taken
    global alphabet
    global turn
    gametypechooser = Tk()
    guessed_letters = []
    available_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lives_taken = 0
    turn = 1
    Label(gametypechooser,text = "Do you want to play against a friend or the computer?").pack()
    Button(gametypechooser,text = "Player vs Player", command=lambda:player_update_board()).pack()
    Button(gametypechooser,text = "Player vs Computer", command=lambda:comporplayerguesserfunction()).pack()
    gametypechooser.mainloop()

def comporplayerguesserfunction():
    comporplayerguesserwindow = Tk()
    Label(comporplayerguesserwindow,text = "Who is guessing the word?").pack()
    Button(comporplayerguesserwindow,text = "Player",command = lambda:player_word_chooser()).pack()
    Button(comporplayerguesserwindow,text = "Computer",command = lambda:computer_word_generator()).pack()
    comporplayerguesserwindow.mainloop()
    
def player_update_board():
    playergame = Tk()
    playergame.wm_title("Hangman")
    playergame.minsize(400,400)
    
    
    
    playergame.mainloop()

def computer_update_board():
    global available_letters
    global alphabet
    global wordlength
    global turn
    computergame = Tk()
    computergame.wm_title("Hangman")
    computergame.minsize(400,400)
    show_hanged_man(lives_taken)
    for n in range(0,26):
        if available_letters[n] == "_":
            labels = Label(computergame, text = alphabet[n],font = ("Impact 17",25),width = 1, height = 1)
            labels.config(fg="red")
            labels.grid(row = 10, column = n, pady = 5)
        else:
            Button(computergame, text = available_letters[n],font = ("Impact 17",25),command=lambda:computer_main(n),width = 2, height = 1).grid(row = 10, column = n, pady = 5)    #row needs to be changed to another number based on the number of things going above the letter buttons/labels
    for n in range(0,wordlength):
        if random_word[n] in guessed_letters:
            Label(computergame,text = random_word[n], font = ("Impact 17", 25)).grid(row = 1,column = n, pady = 5)
        else:
            Label(computergame,text = "______").grid(row = 1,column = n, pady = 5)
    computergame.mainloop()

def computer_main(guess):
    global random_word
    if available_letters[guess] in random_word:
        available_letters[guess] == "_"
        guessed_letters.append(available_letters[guess])
        print(available_letters)
        print(guessed_letters)
        computer_update_board()
        #change button to green 
        #change letter to guessed letters list guessed_letters.append(guess)
        #change letter spot in origional list to "_" available_letters.remove(guess)
    elif available_letters[guess] not in random_word:
        available_letters[guess] == "_"
        guessed_letters.append(available_letters[guess])
        print(available_letters)
        print(guessed_letters)
        computer_update_board()
        #change button to red
        #change letter to guessed letters list guessed_letters.append(guess)
        #change letter spot in origional list to "_" available_letters.remove(guess)
        j=3

def show_hanged_man(x):
    g=1
    #put in here the code to show the image based on the number of lives taken

def computer_word_generator():
    global wordlength
    global random_word
    data = json.load(open('words.json'))
    words_list = list(data["words"].keys())
    random_number = random.randint(0, len(words_list))
    random_word = words_list[random_number]
    print(random_word)
    wordlength = len(random_word)
    computer_update_board()

def player_word_chooser():
    wordchooser = Tk()
    data = json.load(open('words.json'))
    words_list = list(data["words"].keys())
    Label(wordchooser, text = "Choose a word").pack()
    Text(wordchooser).pack()
    wordchooser.mainloop()


start()