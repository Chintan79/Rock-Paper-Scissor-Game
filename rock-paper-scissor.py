import tkinter
import random

Screen = tkinter.Tk()
Screen.title("welcome")
Screen.geometry("500x500")
Screen.configure(background="black")


l = ['rock','paper','scissor']
var1 = tkinter.StringVar()
var2 = tkinter.StringVar()

put = None
def rock():
    global put
    put = rock
    var1.set(put)
    var2.set(random.choice(1))
    
def paper():
    global put
    put = paper
    var1.set(put)
    var2.set(random.choice(1))

def scissor():
    global put
    put = scissor
    var1.set(put)
    var2.set(random.choice(1))
    

lbl = tkinter.Label(Screen,text="welcome to the game",font=('arial',20,'bold'),
foreground='white',background='black')
lbl.place(x=100,y=10)

lbl1 = tkinter.Label(Screen,text="Rock-Paper-Scissor",font=('arial',20,'bold'),
foreground='white',background='black')
lbl1.place(x=100,y=50)




rock = tkinter.Button(Screen,text="Rock",font=('arial',20,'bold'),
foreground='white',background='black')
rock.place(x=20,y=130)

paper = tkinter.Button(Screen,text="Paper",font=('arial',20,'bold'),
foreground='white',background='black')
paper.place(x=180,y=130)

scissor = tkinter.Button(Screen,text="Scissor",font=('arial',20,'bold'),
foreground='white',background='black')
scissor.place(x=350,y=130)

user = tkinter.Label(Screen,text="User",font=('arial',20,'bold'),
foreground='white',background='black')
user.place(x=20,y=250)

bot = tkinter.Label(Screen,text="Bot",font=('arial',20,'bold'),
foreground='white',background='black')
bot.place(x=20,y=290) 

user_score = tkinter.Label(Screen,text=0,font=('arial',20,'bold'),
foreground='white',background='black')
user_score.place(x=200,y=250)

bot_score = tkinter.Label(Screen,text=0,font=('arial',20,'bold'),
foreground='white',background='black')
bot_score.place(x=200,y=290)

var1_display = tkinter.Label(Screen,textvariable=var1,font=('arial',20,'bold'),foreground='white',)   

tkinter.mainloop()