#---------------------------- IMPORTS ----------------------------------------------
from asyncio import events
from email.mime import image
import tkinter as tk
from tokenize import Pointfloat
from turtle import up 
import winsound
import random
#---------------------------- CONSTANT ---------------------------------------------

WINDOW_WIDTH = 1430 
WINDOW_HEIGHT = 750 

COCONUT = 2
APPLE = 3
WATER = 4
VIRUS = 7


#------------------------------ MAIN -----------------------------------------------
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.title("Yummy")
icon=tk.PhotoImage(file="images\Doctorlevel2.png")
root.iconphoto(True,icon)
canvas = tk.Canvas(root)
doctor = tk.PhotoImage(file="images\Doctor.png")
chose= tk.PhotoImage(file="images\Choselevel.png")
level1bg= tk.PhotoImage(file="images\Level1bg.png")
bgwin= tk.PhotoImage(file="images\Bgwin.png")
doctorlevel =tk.PhotoImage(file="images\Doctorlevel2.png")
boxlevel= tk.PhotoImage(file="images\Box level1.png")
bglose= tk.PhotoImage(file="images\Bglose.png")
virus = tk.PhotoImage(file="images\Virus.png")
#----------------------------------- Fruits-----------------------------------------------------
apple = tk.PhotoImage(file = "images\Apple.png")
water = tk.PhotoImage(file = "images\Water.png")
coconut = tk.PhotoImage(file = "images\Coconut.png")

#___________________________________ Instruction ____________________________________

intruction = tk.PhotoImage(file="images\Instruc.png")
bgupdate = tk.PhotoImage(file="images\Bgupdate.png")
rlud = tk.PhotoImage(file="images\Button.png")

#__________________________________grid_______________________________________________

gridlevel1=[[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 0, 0, 5, 0, 0, 7, 0, 0, 2, 0, 7, 5, 0, 0, 0, 2, 4, 0, 0, 0, 0, 2, 5],
            [5, 4, 7, 5, 0, 0, 3, 3, 7, 0, 3, 0, 5, 0, 7, 5, 0, 0, 7, 5, 5, 0, 0, 5],
            [5, 4, 0, 5, 5, 4, 0, 5, 5, 5, 5, 0, 5, 3, 4, 5, 0, 3, 0, 5, 2, 0, 0, 5],
            [5, 0, 0, 0, 5, 3, 3, 0, 0, 4, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 5, 0, 2, 5],
            [5, 0, 2, 4, 5, 5, 0, 0, 7, 0, 7, 3, 7, 0, 4, 0, 0, 3, 7, 0, 0, 5, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 2, 5, 4, 0, 0, 0, 2, 0, 7, 0, 0, 0, 2, 0, 7, 0, 5],
            [5, 5, 5, 5, 7, 0, 0, 0, 5, 0, 0, 7, 5, 5, 4, 0, 0, 4, 5, 0, 0, 0, 0, 5],
            [5, 2, 0, 5, 4, 0, 7, 3, 5, 5, 5, 0, 0, 7, 3, 0, 5, 5, 5, 0, 0, 0, 3, 5],
            [5, 0, 0, 0, 0, 0, 5, 5, 5, 0, 7, 0, 0, 0, 0, 3, 5, 3, 0, 4, 0, 5, 5, 5],
            [5, 1, 0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 7, 2, 4, 0, 5, 5, 5, 5, 0, 0, 2, 5],
            [5, 5, 5, 5, 0, 4, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 5],
            [5, 0, 0, 3, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 7, 0, 5, 5, 5, 0, 7, 5],
            [5, 7, 0, 0, 0, 2, 0, 0, 7, 0, 2, 0, 4, 0, 0, 3, 0, 0, 5, 3, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]

#--------------------------------- functions ---------------------------------------------
notWin = True
def drawing1():
    if notWin:
        global timelabel,powerLabel,power
        canvas.delete("doctor1")
        for row in range(len(gridlevel1)):
            for column in range(len(gridlevel1[row])):
                if gridlevel1[row][column] == 1:
                    canvas.create_image(100 + column*35, row*35 + 97, image = doctorlevel ,tags = "doctor1")
                elif gridlevel1[row][column] == 5:
                    canvas.create_image(97 + column*35, row*35 + 97, image = boxlevel ,tags = "doctor1")
                if gridlevel1[row][column] == 2:
                    canvas.create_image(97 + column*35, row*35 + 97, image = coconut ,tags = "doctor1")
                if gridlevel1[row][column] == 3:
                    canvas.create_image(97 + column*35, row*35 + 97, image = apple ,tags = "doctor1")
                if gridlevel1[row][column] == 4:
                    canvas.create_image(97 + column*35, row*35 + 97, image = water ,tags = "doctor1")
                if gridlevel1[row][column] == 7:
                    canvas.create_image(97 + column*35, row*35 + 97, image = virus ,tags = "doctor1")


#__________________________________________fuunction power_______________________________

power=0
def powerCounter():
    global power
    canvas.itemconfig(powerLabel, text = "Power: " + str(power) + "/450", anchor= 'se')
    canvas.after(10, powerCounter)
powerLabel = canvas.create_text(180, 70, text =power, font=('Peach Days', 24, 'bold'), fill='black')

#_____________________________________fuunction defind character position_______________________________

def getIndexSuzy():
    global power,r,col,row,column
    for r in range(len(gridlevel1)):
        for col in range(len(gridlevel1[r])):
            if gridlevel1[r][col] == 1:
                row = r
                column = col
    return[ row, column]

#__________________________________________fuunction move character and sum power_______________________________

def move(direction):
    global power, row, column, notWin
    indexlevel1 = getIndexSuzy()
    rowLine = indexlevel1[0]
    columnLine = indexlevel1[1]
    notWin = True

    if direction == "right":
        if columnLine != len(gridlevel1[rowLine]) - 1 and gridlevel1[rowLine][columnLine + 1] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine][columnLine + 1] == COCONUT:
                power += 10
            if  gridlevel1[rowLine][columnLine + 1] == APPLE:
                power += 15
            if  gridlevel1[rowLine][columnLine + 1] == WATER:
                power += 5
            if  gridlevel1[rowLine][columnLine + 1] == VIRUS:
                power -= 10
            gridlevel1[rowLine][columnLine + 1] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    elif direction == "left":
        if columnLine != 0 and gridlevel1[rowLine][columnLine - 1] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine][columnLine - 1] == COCONUT:
                power += 10
            if  gridlevel1[rowLine][columnLine - 1] == APPLE:
                power += 15
            if  gridlevel1[rowLine][columnLine - 1] == WATER:
                power += 5
            if  gridlevel1[rowLine][columnLine - 1] == VIRUS:
                power -= 10
            gridlevel1[rowLine][columnLine - 1] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            
    elif direction == "up":
        if rowLine != 0 and gridlevel1[rowLine - 1][columnLine] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine - 1][columnLine ] == COCONUT:
                power += 10
            if  gridlevel1[rowLine - 1][columnLine ] == APPLE:
                power += 15
            if  gridlevel1[rowLine - 1][columnLine ] == WATER:
                power += 5
            if  gridlevel1[rowLine - 1][columnLine ] == VIRUS:
                power -= 10
                winsound.PlaySound("sound\\Eating.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            gridlevel1[rowLine - 1][columnLine] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    elif direction == "down":
        if rowLine != len(gridlevel1) - 1 and gridlevel1[rowLine + 1][columnLine] != 5:
            gridlevel1[rowLine][columnLine] = 0
            if  gridlevel1[rowLine+ 1][columnLine ] == COCONUT:
                power += 10
            if  gridlevel1[rowLine+ 1][columnLine ] == APPLE:
                power += 15
            if  gridlevel1[rowLine+ 1][columnLine ] == WATER:
                power += 5
            if  gridlevel1[rowLine+ 1][columnLine ] == VIRUS:
                power -= 10
            gridlevel1[rowLine + 1][columnLine] = 1
            winsound.PlaySound("sound\\Move.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    if power >= 450:
        notWin = False
        youWin()
    elif power < 0 or minute == 1:
        notWin = False
        youLose()
    drawing1()  

#____________________________Move character____________________________________________

def moveRight(event):
    move("right")

def moveLeft(event):
    move("left")

def moveUp(event):
    move("up")

def moveDown(event):
    move("down")
#__________________________________________fuunction Win_______________________________

def youWin():
    global notWin
    notWin = False
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image = bgwin)
    winsound.PlaySound("sound\\Win.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_text(660, 325, text = "You WON!", font=('consolas 15', 50, 'bold'), fill='yellow')
    canvas.create_text(650, 400, text = "Your Score: " + str(power) + " Point", font=('consolas', 25, 'bold'), fill='white')
    canvas.create_text(650, 450, text = "Time: " + str(minute) + ":" + str(time) + "s", font=('consolas', 25, 'bold'), fill='white')
    canvas.create_text(150,680,text='Back',anchor='se',font=('consolas 15Peach Days', 30,'underline'), fill='black', tags="back")
    canvas.create_text(1300,680,text="Exit",anchor='se', font=('consolas 15', 30,'underline'), fill='black',tags='exit')
    
#__________________________________________fuunction lose_______________________________

def youLose():
    global notWin
    notWin = False
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image = bglose)
    winsound.PlaySound("sound\\Lost.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_text(660, 325, text = "You LOSE!", font=('consolas 15', 40, 'bold'), fill='#1475DC')
    canvas.create_text(650, 400, text = "Your Score: " + str(power) + " Point", font=('consolas', 15, 'bold'), fill='white')
    canvas.create_text(650, 450, text = "Time: " + str(minute) + " : " + str(time) + "s", font=('consolas', 15, 'bold'), fill='white')
    canvas.create_text(150,680,text='Back',anchor='se',font=('consolas 15', 30,'underline'), fill='white', tags="back")
    canvas.create_text(1300,680,text="Exit",anchor='se', font=('consolas 15', 30,'underline'), fill='white',tags='exit')


#__________________________________________fuunction countime_______________________________


notWin=True   
minute = 0
time = 0
def timeCounter():
    global time, minute
    if time == 60:
        minute += 1
        time = 0
    time += 1
    canvas.itemconfig(timelabel, text = "Time: " + str(minute) + " : " + str(time) + "s")
    canvas.after(1000, timeCounter)
timelabel = canvas.create_text(100, 70, text = time, font=('consolas', 24, 'bold'), fill='white')

def level1(event):
    global powerCounter,timeCounter,timelabel,powerLabel,drawing1
    canvas.delete('all')
    winsound.PlaySound("sound\\Level1.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    powerCounter()
    timeCounter()
    canvas.create_image(0,0,anchor="nw",image = level1bg)
    canvas.create_text(1120,100,text="Intructions",font=('Peach Days', 30), fill='black')
    canvas.create_image(1125,380,image=intruction)
    canvas.create_text(150,680,text='Back',anchor='se',font=('consolas 15', 30,'underline'), fill='black', tags="back")
    timelabel = canvas.create_text(200, 50, text = time, font=('consolas 15', 24), fill='black')
    powerLabel = canvas.create_text(800, 70, text = power, font=('consolas 15', 24), fill='black')
    drawing1()
    
#----------------------------------- Start game------------------------------------------------

def chooseLevel(event):
    canvas.delete('all')
    winsound.PlaySound("sound\\Tik tik.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,anchor='nw',image=chose)
    canvas.create_text(900,180,text="Choose level" ,anchor='se',font=('Peach Days', 50, 'bold'),fill='white' )
    canvas.create_text(750,360,text="Level1",anchor='se',font=('Peach Days', 40, 'bold'), fill='black', tags="level1")
    canvas.create_text(750,490,text="Level2",anchor='se',font=('Peach Days', 40, 'bold'), fill='black', tags="level2")
    canvas.create_text(750,610,text="Level3",anchor='se',font=('Peach Days', 40, 'bold'), fill='black', tags="level3")
    canvas.create_text(280,655,text='Back',anchor='se',font=('consolas 15', 30, 'underline'), fill='white', tags="back")

def startGame(event):
    canvas.delete('all')
    winsound.PlaySound("sound\\Start.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(0,0,anchor='nw',image=doctor)
    canvas.create_text(980,175,text="Welcome to YUMMY" ,anchor='se',font=('Peach Days', 50, 'bold'),fill='yellow' )
    canvas.create_text(740,350,text="Start",anchor='se',font=('Peach Days', 40, 'bold'), fill='white', tags="start")
    canvas.create_text(740,465,text="Help",anchor='se', font=('Peach Days', 40, 'bold'), fill='white',tags='rule')
    canvas.create_text(720,585,text="Exit",anchor='se', font=('Peach Days', 40, 'bold'), fill='white',tags='exit')

def rule(event):
    canvas.delete('all')
    canvas.create_image(0,0,anchor='nw',image=bgupdate)
    canvas.create_rectangle(150, 150,1200,600, outline="pink", fill="white")
    canvas.create_text(645,250, text = "You need to use these 4 buttons to move SUZY", fill="black", font=("consolas 15 bold",24))
    canvas.create_image(670,400,image=rlud)
    canvas.create_text(1160,180, text = "x", fill="red", font=("Peach Days ", 40 ,'bold'), tags='Back' )

canvas.tag_bind('Back',"<Button-1>",startGame) 

def exitedGame(event):
    root.quit()
canvas.tag_bind('exit',"<Button-1>",exitedGame)

#________________________________________________Function update For level 2,3__________________________________________
def update(event):
    canvas.delete('all')
    canvas.create_image(0,0,anchor='nw',image=bgupdate)
    canvas.create_rectangle(400, 150,950,300, outline="pink", fill="white")
    canvas.create_text(650,200, text = "Try again!", fill="black", font="consolas 15 bold")
    canvas.create_text(650,230, text = "This level we are Updating.", fill="black", font="consolas 15")
    canvas.create_text(650,260, text = "...", fill="black", font="consolas 15")
    canvas.create_text(920,170, text = "X", fill="red", font=("Peach Days ", 20 ,'bold'), tags='delete' )

canvas.tag_bind('level2',"<Button-1>",update)
canvas.tag_bind('level3',"<Button-1>",update)
canvas.tag_bind('delete',"<Button-1>",chooseLevel)


startGame(event=startGame)

canvas.pack(expand=True, fill='both')

canvas.tag_bind('rule',"<Button-1>",rule)
canvas.tag_bind('back',"<Button-1>",startGame)
canvas.tag_bind('start',"<Button-1>",chooseLevel)
canvas.tag_bind('level1',"<Button-1>",level1)
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)

root.mainloop()