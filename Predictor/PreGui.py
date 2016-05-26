import tkinter

buttons = []
window = tkinter.Tk()
window.geometry('{}x{}'.format(200, 300))

def doStuff():
    print("lol")



def changeWords(word):
    for b in range(len(buttons)):
        buttons[b].destroy()

    for i in word:
        buttons.append(tkinter.Button(window, text = i, command = doStuff))

        buttons[len(buttons)-1].pack()


changeWords(["hej", "med", "dig"])

window.mainloop()
