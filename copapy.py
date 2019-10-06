from tkinter import Tk, Frame, BOTH, Menu, TclError, Label, RAISED, SUNKEN, SOLID, messagebox

class Copapy(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self, parent, height=800, width=600)
        parent.title("copapy - copy & paste history")
        # parent.resizable(False, False)
        self.pack_propagate(0)
        self.pack()

if __name__ == '__main__':
    root = Tk()
    Copapy = Copapy(root)
    Copapy.mainloop()
