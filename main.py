import tkinter as tk
import random
#functions

dumbness = 5

jeffsayings = {"mrrrrrp", "grrrrrr", "murp", "gurp", "RAWR", "MRRRRRRRRRf"}


def leave():
    root.destroy()

def messup(a):
    global dumbness
    x = random.randint(-dumbness,dumbness)
    if x == 0:
        x = list(jeffsayings)[0]
    return x

def add(a, b):
    x = a + b
    return x

def minus(a, b):
    x = a - b
    return x

def times(a, b):
    x = a * b
    return x

def divide(a, b):
    x = a / b
    return x

def solve():
    x = entrybox.get()
    x = x.split()
    a = int(x[0])
    s = x[1]
    b = int(x[2])

    if s == "+":
        d = add(a, b))
    elif s == "-":
        d = minus(a, b)
    elif s == "*":
        d = times(a, b)
    elif s == "/" or s == "%":
        d = divide(a, b)
    else:
        d = "Error"
        awnser.config(text = d)


#window set up / settings
root = tk.Tk()
root.title("JeffDoesMath")
root.geometry("200x300")

#widgits being created
exitb = tk.Button(root, command = leave, text = "exit")
entrybox = tk.Entry(root, width = 15,)
solvebutton = tk.Button(root, command = leave, text = "solve")
awnser = tk.Label(root, text = list(jeffsayings)[0])

#add widget to windows :3
exitb.place(x=175, y=250)
entrybox.place(x= 0, y=75)
solvebutton.place(x=0, y=100)
awnser.place(x=0, y=25)



root.mainloop()


