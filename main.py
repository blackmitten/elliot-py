from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.menubar = Label(master, text="This is where the menu bar will be")
        self.menubar.grid(row=0,columnspan=2, sticky=W)

        self.board_control = Canvas(master, width=400, height=400)
        self.board_control.grid(row=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, columnspan=2)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()