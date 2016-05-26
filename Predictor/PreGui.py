import tkinter

buttons = []
window = tkinter.Tk()
window.geometry('{}x{}'.format(200, 300))

def doStuff():
    print("lol")



def changeWords():
    for i in ["hej", "med", "dig"]:
        buttons.append(tkinter.Button(window, text = i, command = doStuff))

        buttons[len(buttons)-1].pack()


changeWords()
window.mainloop()
