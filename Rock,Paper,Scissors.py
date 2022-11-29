# ==================imports=================
from tkinter import *
from random import choice
from tkinter import messagebox
from os import getcwd
#===================logic1===================
playermove = ""
points = {"computer" : 0, "player" : 0}
computermove = ""
# ==================settings================
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x648")
root.resizable(width = True, height = True)
bgcolor = "#faf88e"
root.configure(bg=bgcolor)
root.iconbitmap(getcwd()+'\edited.ico')
#====================Frame==================
def frameCreator():
    newFrame = Frame(root, bg = bgcolor, width=500, height=81)
    return newFrame
Top_one = frameCreator()
Top_one.pack(side = "top")
Top_two = frameCreator()
Top_two.pack(side = TOP)
Top_three = frameCreator()
Top_three.pack(side = "top")
Top_four = frameCreator()
Top_four.pack(side = "top")
Top_five = frameCreator()
Top_five.pack(side = "top")
Top_six = Frame(root, bg = bgcolor, width=500, height=40)
Top_six.pack(side = "top")
Top_seven = frameCreator()
Top_seven.pack(side = "top")
Top_seven_left =  Frame(Top_seven, bg = bgcolor, width=250, height=81)
Top_seven_left.pack(side="left", pady= 20)
Top_seven_right =  Frame(Top_seven, bg = bgcolor, width=250, height=81)
Top_seven_right.pack(side="right", pady= 20)
Top_eight = frameCreator()
Top_eight.pack(side = "top")
#=================functions=================
result = Label(Top_seven_left, bg=bgcolor, fg="#636359", 
font= ("times new roman", 25, "italic", "bold"), text="")
def gameLogic(computermove, playermove, goals):
    if computermove == "Rock":
        if playermove == "rock":
            result.configure(text = "tie")
        elif playermove == "paper":
            result.configure(text = "win")
            goals["player"] += 1
        elif playermove == "scissors":
            result.configure(text = "lose")
            goals["computer"] += 1
    elif computermove == "Paper":
        if playermove == "rock":
            result.configure(text = "lose")
            goals["computer"] += 1
        elif playermove == "paper":
            result.configure(text = "tie")
        elif playermove == "scissors":
            result.configure(text = "win")
            goals["player"] += 1
    elif computermove == "Scissors":
        if playermove == "rock":
            result.configure(text = "win")
            goals["player"] += 1
        elif playermove == "paper":
            result.configure(text = "lose")
            goals["computer"] += 1
        elif playermove == "scissors":
            result.configure(text = "tie")
    else: # in order to debug
        print("None of the computer move")
    result.pack(padx=60)
    return goals
lbl3 = Label(Top_six, font=("TimesNewRoman", 22, "italic", "bold"), bg=bgcolor)  # showes computer's move to user
lblScores = Label(Top_seven_right, text = f'computer: {points["computer"]}\nyou: {points["player"]}', 
font=("calibri", 15, "bold", "italic"))
def rockPlayed(points):
    playermove = "rock"
    computermove = choice(["Rock", "Paper", "Scissors"]) #choose computer's move
    lbl3.configure(text=computermove)
    lbl3.pack()
    points = gameLogic(computermove, playermove, points)
    lblScores.configure(text=f'computer: {points["computer"]}\nyou: {points["player"]}')
    lblScores.pack(side = "right")
def paperPlayed(points):
    playermove = "paper"
    computermove = choice(["Rock", "Paper", "Scissors"]) #choose computer's move
    lbl3.configure(text=computermove)
    lbl3.pack()
    points = gameLogic(computermove, playermove, points)
    lblScores.configure(text=f'computer: {points["computer"]}\nyou: {points["player"]}')
    lblScores.pack(side = "right")
def scissorsPlayed(points):
    playermove = "scissors"
    computermove = choice(["Rock", "Paper", "Scissors"]) #choose computer's move
    lbl3.configure(text=computermove)
    points = gameLogic(computermove, playermove, points)
    lblScores.configure(text=f'computer: {points["computer"]}\nyou: {points["player"]}')
    lblScores.pack(side = "right")
    lbl3.pack()
def creator():
    messagebox.showinfo("Creator", "Aria Hani\nEmail: aria.hani.t@gmail.com")
def reset(points):
    points["computer"] = 0
    points["player"] = 0
    lblScores.configure(text=f'computer: {points["computer"]}\nyou: {points["player"]}')
    lblScores.pack(side = "right")
    lbl3.configure(text="")
    result.configure(text="     ")
#====================buttons================
def btnCreator(frame, script, command):
    return Button(frame, text=script, width=20, height=1, bg = "#d6f2b6",
    fg = "#bb6ce0", font = ("Calibri", 26, "bold"), command=command)

btnRock = btnCreator(Top_two, "Rock", lambda: rockPlayed(points))
btnRock.pack()
btnPaper = btnCreator(Top_three, "Paper", lambda: paperPlayed(points))
btnPaper.pack()
btnScissors = btnCreator(Top_four, "Scissors", lambda: scissorsPlayed(points))
btnScissors.pack()
btnLicense = Button(Top_eight, text="Developer", font=("Arial", 15, "bold"), 
fg="#3e4232", bg="#e6aa91", command= lambda : creator())
btnLicense.pack(side="left", padx=70)
btnReset = Button(Top_eight, text="Reset", font=("Arial", 15, "bold"), 
fg="#3e4232", bg="#e6aa91", command= lambda : reset(points))
btnReset.pack(side="left", padx=70)
#==================labels===================
def lblCreator(window, text):  # used window not to be confused with root the main window
    return Label(window, text=text, font = ("calibri", 26, "bold", "italic"), 
    fg="#eaff00", bg="#000000", height=1)
lbl1 = lblCreator(Top_one, "Choose one of the followings:")
lbl1.pack(padx=5, pady=25)
lbl2 = lblCreator(Top_five, "Computer's move is:")
lbl2.pack(padx=5, pady=25)
#====================run====================
root.mainloop()