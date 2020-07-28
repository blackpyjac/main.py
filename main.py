from tkinter import *
import getpass

#defining the main window 
mainWindow=Tk()
mainWindow.title("TicTacToe")
mainWindow.call('wm', 'iconphoto', mainWindow._w, PhotoImage(file='assets/ico_tictactoegame.png'))
mainWindow.geometry("1024x600")
mainWindow.resizable(0,0)
mainButtons=True
img=PhotoImage(file="assets/titotacgamev2logo.png")
bl=Label(mainWindow,image=img)
bl.place(x=0,y=0, relwidth=1, relheight=1)
message = Label( mainWindow, text="¡Welcome %s to TIC-TAC-TOE game!\t"%getpass.getuser().capitalize(), font='Cezanne 20 bold', fg='#e5f492',background='#083648', height=1, width=50)
message.place(x=170,y=2)
def create_buttons():
    if mainButtons:
        _option = Button(mainWindow, text="Play vs computer", font='Times 12 bold', bg='#bfda32', fg='#083648', height=2, width=30,activebackground='#083648',activeforeground='#bfda32',borderwidth=2,cursor='hand1' ,command=lambda: humanvshuman())
        _option.place(x=350,y=220)

        option1 = Button(mainWindow, text="Play vs another player", font='Times 12 bold', bg='#7dccec', fg='#083648', height=2, width=30,activebackground='#083648',activeforeground='#7dccec',borderwidth=2,cursor='hand1' ,command=lambda: c())
        option1.place(x=350,y=280)
        about = Button(mainWindow, text="About", font='Times 12 bold', bg='orange', fg='white', height=2, width=30,activebackground='white',activeforeground='orange',borderwidth=2,cursor='hand1' ,command=lambda: humanvshuman())
        about.place(x=350,y=340)
        option2 = Button(mainWindow, text="Exit", font='Times 12 bold', bg='red', fg='white', height=2, relief='flat',width=30,activebackground='white',activeforeground='red',borderwidth=2,cursor='hand1',overrelief='raised', command=mainWindow.quit)
        option2.place(x=350,y=400)
    else:
        option2 = Button(mainWindow, text="Exit", font='Times 12 bold', bg='red', fg='white', height=2, relief='flat',width=30,activebackground='white',activeforeground='red',borderwidth=2,cursor='hand1',overrelief='raised', command=mainWindow.quit)
        option2.place(x=350,y=400)

def humanvshuman():
    mainButtons=False
    create_buttons()
    print("entro")

create_buttons()    
mainWindow.mainloop()