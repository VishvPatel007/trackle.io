from Tkinter import *        
import tkMessageBox
import click
import main


speech = False

def openInfo():
    
    info = Tk()
    info.title("Learn more about trackle.io")
    info.geometry('450x200+200+200')
    info.configure(background='white')

    
    label1 = Label(info, text="trackle.io was created as a keyboard and mouse replacement\n for individuals with disabilities and restricted movement capabilities.\n\nOne such condition is carpal tunnel which affects 8 million people yearly\nand trackle.io can be used as both a recovery and prevention tool.\n\nAlong with that, it is a platform for enthusiasts looking for an\n alternative way to interact with their computers including gamers and students.", height=10)
    label1.pack()
    label1.configure(background='white')
    button1 = Button(info, text="Exit", width=10, command=info.destroy)
    button1.pack(padx=15, pady=15)

    info.mainloop()

    return

def chooseClick():
    radioValue = clickType.get()
    
    if clickType.get() == "Key":
        name = "You have selected key input with the character '" + inType.get() +"'."
        main.setInput(inType.get())
    else:
        name = "You have selected wink input."
        main.clearInput()
    labelText2.set(name)
    return

def speechSet():
    global speech
    if speech == False:
        name = "The speech to text function is on."
        speech = True
        click.enableDisable()
    else:
        name = "The speech to text function is off."
        speech = False
        click.enableDisable()
    labelText3.set(name)
 


def init():    
    app = Tk()
    app.title("trackle.io")
    app.geometry('450x550+100+50')
    app.configure(background='white')

    labelText = StringVar()
    labelText.set("Welcome to trackle.io.\n\n This application is a full keyboard and mouse replacement\nthat uses speech to text input and\neither a key input or wink to register a 'click'.")
    label1 = Label(app, textvariable=labelText, height=6)
    label1.configure(background='white')
    label1.pack()

    button2 = Button(app, text="Learn more", width=20, command=openInfo)
    button2.pack(padx=15, pady=15)

    labelText2 = StringVar()
    labelText2.set("Choose a 'click' type to get started.")
    label2 = Label(app, textvariable=labelText2, height=4)
    label2.configure(background='white')
    label2.pack()

    clickType = StringVar()
    clickType.set(None)
    radio1 = Radiobutton(app, text="Wink", value="Wink", variable = clickType).pack()

    radio2 = Radiobutton(app, text="Key (enter the key below)", value="Key", variable = clickType).pack()

    keyType = StringVar(None)
    inType = Entry(app, textvariable=keyType)
    inType.configure(background='white')
    inType.pack()


    button1 = Button(app, text="Start", width=20, command=chooseClick)
    button1.pack(padx=15, pady=15)

    labelText3 = StringVar()
    labelText3.set("The speech to text function is off.")
    label3 = Label(app, textvariable=labelText3, height=2)
    label3.configure(background='white')

    label3.pack()

    button2 = Button(app, text="Speech to text on/off", width=20, command=speechSet)
    button2.pack(padx=15, pady=5)


    button3 = Button(app, text="Exit", width=10, command=app.destroy)
    button3.pack(padx=15, pady=25)

    photo = PhotoImage(file = 'trackle.pbm')
    label4 = Label(image=photo)
    label4.image = photo
    label4.configure(background='white')
    label4.pack()

    app.mainloop()
