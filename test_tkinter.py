# need Tkinter for 2.7 or tkinter for 3.0
from Tkinter import *
print ("I have started")

def print_oli():
    print("Olivier")
    label2["text"] = "Answer : Oli"
    

def print_dehon():
    print("Dehon")
    label2["text"] = "Answer : Dehon"
    

root = Tk()
label = Label(root, text="Hello in the window")
label.pack()

label2 = Label(root, text="Answer : xx")
label2.pack()

button = Button(root, text="Push Here", command=print_oli)
button.pack()
button2 = Button(root, text="Or Here !", command = print_dehon)
button2.pack()






root.mainloop()

print("I am finished")

