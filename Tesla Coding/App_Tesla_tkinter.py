# need Tkinter for 2.7 or tkinter for 3.0
from Tkinter import *
print ("App has started")





def print_oli():
    print("Olivier")
    label2["text"] = "Answer : Oli"
    

def print_dehon():
    print("Dehon")
    label2["text"] = "Answer : Dehon"
    

def check_data():
	print("Checking Data")
	label2["text"] = "Checking Data Now..."


root = Tk()
label = Label(root, text="Remote Access to Tesla")
label.pack()

label2 = Label(root, text="Answer : xx")
label2.pack()

button = Button(root, text="Check Data", command=check_data)
button.pack()
button2 = Button(root, text="Send me Email of Data", command = print_dehon)
button2.pack()






root.mainloop()

print("I am finished")

