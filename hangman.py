from tkinter import *
import time

def start():
    global available_letters
    global guessed_letters
    global lives_taken
    global alphabet
    gametypechooser = Tk()
    guessed_letters = []
    available_letters = ["A","B","C","D","E","F","_","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Y","Z"]
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Y","Z"]
    lives_taken = 0
    Label(gametypechooser,text = "Do you want to play against a friend or the computer?").pack()
    Button(gametypechooser,text = "Player vs Player", command=lambda:player_update_board()).pack()
    Button(gametypechooser,text = "Player vs Computer", command=lambda:computer_update_board()).pack()
    gametypechooser.mainloop()


def update_board():
    global wordlength
    root = Tk()
    root.minsize(400,400)
    root.wm_title("Hangman")
    for n in range(0,wordlength):
        Label(root,text = "______").place(x= (20 * n) + 20 ,y=200)



    root.mainloop()
    
def player_update_board():
    playergame = Tk()
    playergame.wm_title("Hangman")
    playergame.minsize(400,400)
    
    
    
    playergame.mainloop()

def computer_update_board():
    global available_letters
    global alphabet
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
            Button(computergame, text = available_letters[n],font = ("Impact 17",25),command=lambda:computer_main(n),width = 1, height = 1).grid(row = 10, column = n, pady = 5)    #row needs to be changed to another number based on the number of things going above the letter buttons/labels
    computergame.mainloop()
    
def player_main():
    g = 3
    
def computer_main(guess):
    #Choose random word out of the list in the dictionary json file and store it to a variable called "chosen_word"
    #if guess in chosen_word:
        #change button to green 
        #change letter to guessed letters list guessed_letters.append(guess)
        #change letter spot in origional list to "_" available_letters.remove(guess)
    #elif guess not in chosen_word:
        #change button to red
        #change letter to guessed letters list guessed_letters.append(guess)
        #change letter spot in origional list to "_" available_letters.remove(guess)
    j=3

def show_hanged_man(x):
    g=1
    #put in here the code to show the image based on the number of lives taken
    Hanger = PhotoImage(file = "Hanger.png")
    Hanger.grid(row = 5 column = 4)
    Head = PhotoImage(file = "Head.png")

    LefArm = PhotoImage(file = "Left Arm.png")

    RightArm = PhotoImage(file = "Right Arm.png")
    
    LeftLeg = PhotoImage(file = "Left Leg.png")

    RightLeg = PhotoImage(file = "Right Leg.png")

    Torso = PhotoImage(file = "Torso.png")

    Noose = PhotoImage(file = "Noose.png")


start()

#need to implement a computer guessing or player guessing choice place and the function for the random letter generation guess =  pick random(0,len(available_letters)) 

##  git config --global user.email "19HAttryde@collegiate.org.uk"   git config --global user.name "attrydeh"