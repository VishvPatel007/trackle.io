from Tkinter import *        
import tkMessageBox


def chooseClick():
    radioValue = clickType.get()
    if clickType.get() == "Key":
        name = "You have selected key input."
    else:
        name = "You have selected wink input"
    labelText2.set(name)  
    return
    
app = Tk()
app.title("trackle.io")
app.geometry('450x400+200+200')

labelText = StringVar()
labelText.set("Welcome to trackle.io.\n\n This application is a full keyboard and mouse replacement\nthat uses speech to text input and\neither a key input or wink to register a 'click'.")
label1 = Label(app, textvariable=labelText, height=6)
label1.pack()

button2 = Button(app, text="Learn more", width=20)
button2.pack(padx=15, pady=15)

labelText2 = StringVar()
labelText2.set("Choose a 'click' type to get started.")
label2 = Label(app, textvariable=labelText2, height=4)
label2.pack()

clickType = StringVar()
clickType.set(None)
radio1 = Radiobutton(app, text="Key", value='Key', variable = clickType).pack()
radio2 = Radiobutton(app, text="Wink", value='Wink', variable = clickType).pack()

button1 = Button(app, text="Start", width=20, command=chooseClick)
button1.pack(padx=15, pady=15)

button2 = Button(app, text="Exit", width=20, command=app.destroy)
button2.pack(padx=15, pady=15)

app.mainloop()
