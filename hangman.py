from tkinter import *
import time
import json
import random
import os
from os import walk
import tkinter as tk

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
    Button(comporplayerguesserwindow,text = "Player",command = lambda:player_word_chooser(0)).pack()
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
    global computergame
    computergame = Toplevel()
    computergame.wm_title("Hangman")
    computergame.minsize(400,400)
    show_hanged_man(lives_taken)
    for n in range(0,26):
        if available_letters[n] == "_":
            labels = Label(computergame, text = alphabet[n],font = ("Impact 17",25),width = 1, height = 1)
            labels.config(fg="red")
            labels.grid(row = 10, column = n, pady = 5)
        else:
            print(n)
            Button(computergame, text = available_letters[n],font = ("Impact 17",25),command=lambda:computer_main(n),width = 2, height = 1).grid(row = 10, column = n, pady = 5)    #row needs to be changed to another number based on the number of things going above the letter buttons/labels
    for n in range(0,wordlength):
        if random_word[n] in guessed_letters:
            Label(computergame,text = random_word[n], font = ("Impact 17", 25)).grid(row = 1,column = n, pady = 5)
        else:
            Label(computergame,text = "______").grid(row = 1,column = n, pady = 5)
    computergame.mainloop()

def computer_main(guess):
    global random_word
    print(guess)
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
    global images
    global computergame
    g=1
    #put in here the code to show the image based on the number of lives taken
    # image1 = Image.open("hangman images\Head.png")
    # image1 = ImageTk.PhotoImage(image1)
    # label1 = Label(image=image1)
    # label1.pack()
    images =[]
    if x == 0:
        HangIm = PhotoImage(file = "hangman images\Hanger.png") 
        Hang = Label(computergame, image=HangIm)
        Hang.place(x= 88, y =140)
        images.append(HangIm)
    
    if x == 1:
        HeadIm = PhotoImage(file = "hangman images\Head.png") 
        Head = Label(computergame, image=HeadIm)
        Head.place(x= 297, y =220)
        images.append(HeadIm)

    if x == 2:
        TorsoIm = PhotoImage(file = "hangman images\Torso.png")
        Torso = Label(computergame, image=TorsoIm)
        Torso.place(x= 100, y =100)
        images.append(TorsoIm)

    if x == 3:
        LeftArmIm = PhotoImage(file = "hangman images\Left Arm.png")  
        LeftArm = Label(computergame, image=TorsoIm)
        LeftArm.place(x= 100, y =100)
        images.append(LeftArmIm)
    if x == 4:
        RightArmIm = PhotoImage(file = "hangman images\Right Arm.png")
        RightArm = Label(computergame, image=RightArmIm)
        RightArm.place(x= 100, y =100)
        images.append(RightArmIm)
    
    if x == 5:
        LeftLegIm = PhotoImage(file = "hangman images\Left Leg.png")
        LeftLeg = Label(computergame, image=LeftArmIm)
        LeftLeg.place(x= 100, y =100)
        images.append(LeftLegIm)

    if x == 6:
        RightLegIm = PhotoImage(file = "hangman images\Right Leg.png")
        RightLeg = Label(computergame, image=RightArmIm)
        RightLeg.place(x= 100, y =100)
        images.append(RightLegIm)


    if x == 7:
        NooseIm = PhotoImage(file = "hangman images\\Noose.png")
        Noose = Label(computergame, image=NooseIm)
        Noose.place(x= 200, y =100)
        images.append(NooseIm)




    

        

    # Head = PhotoImage(file = "hangman images\Head.png")

    # LefArm = PhotoImage(file = "Left Arm.png")

    # RightArm = PhotoImage(file = "Right Arm.png")
    
    # LeftLeg = PhotoImage(file = "Left Leg.png")

    # RightLeg = PhotoImage(file = "Right Leg.png")

    # Torso = PhotoImage(file = "Torso.png")

    # Noose = PhotoImage(file = "Noose.png")

def computer_word_generator():
    global wordlength
    global random_word
    global words_list
    data = json.load(open('words.json'))
    words_list = list(data["words"].keys())
    random_number = random.randint(0, len(words_list))
    random_word = words_list[random_number]
    print(random_word)
    wordlength = len(random_word)
    computer_update_board()

def player_word_chooser(type):
    global word_enterer
    global words_list
    if type == 0:
        wordchooser = Tk()
        data = json.load(open('words.json'))
        words_list = list(data["words"].keys())
        Label(wordchooser, text = "Choose a word").pack()
        word_enterer = Text(wordchooser).pack()
        Button(wordchooser,text = "Submit word.").pack()
        wordchooser.mainloop()
    elif type == 1:
        wordchooser = Tk()
        data = json.load(open('words.json'))
        words_list = list(data["words"].keys())
        Label(wordchooser, text = "Choose a different word").pack()
        word_enterer = Text(wordchooser).pack()
        Button(wordchooser,text = "Submit word.", command = lambda:player_word_checker()).pack()
        wordchooser.mainloop()


def player_word_checker():
    global words_list
    global word_enterer
    word_in = word_enterer.get(1.0,"end-1c")
    if word_in.lower() not in words_list:
        player_word_chooser(1)
    else:
        computer_update_board()

start()

#need to implement a computer guessing or player guessing choice place and the function for the random letter generation guess =  pick random(0,len(available_letters)) 

##  git config --global user.email "19HAttryde@collegiate.org.uk"   git config --global user.name "attrydeh"