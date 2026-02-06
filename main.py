import tkinter as tk
#functions


def leave():
    root.destroy()

def add(a, b):
    x = a + b
    return x





#window set up / settings
root = tk.Tk()
root.title("JeffDoesMath")
root.geometry("200x300")

#widgits being created
exitb = tk.Button(root, command = leave, text = "exit")
entrybox = tk.Entry(root, width = 15,)

#add widget to windows :3
exitb.place(x=175, y=250)
entrybox.place(x= 75, y=0)



root.mainloop()


