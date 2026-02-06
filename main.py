import tkinter as tk
import random
#functions

dumbness = 20

jeffsayings = {"mrrrrrp", "grrrrrr", "murp", "gurp", "RAWR", "MRRRRRRRRRf", "BLAARGGULARG", "AHHHHbabababababa", "eaaaarrrgghhh", "*shows Ming the Cowculator at https://github.com/Knights-of-Dev/Ming-the-Cowculator*"}


def error():
    pass

def leave():
    root.destroy()

def messup(d):
    
    global dumbness
    global jeffsayings
    x = random.randint(-dumbness,dumbness)
    if x == 0:
        x = list(jeffsayings)[0]
    else:
        x = d + x
    x = str(x)
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
    global jeffsayings
    x = entrybox.get()
    x = x.split()
    if len(x) == 3:
        a = int(x[0])
        s = x[1]
        b = int(x[2])

    

        if s == "+":
            d = add(a, b)
            t = True
        elif s == "-":
            d = minus(a, b)
            t = True
        elif s == "*":
            d = times(a, b)
            t = True
        elif s == "/" or s == "%":
            d = divide(a, b)
            t = True
        else:
            t = False
            d = list(jeffsayings)[0]
            awnser.config(text = d)
    
        if t == True:
            isdumb = random.randint(1,10)
            if isdumb == 1:
                d = messup(d)
                awnser.config(text = d)
            else:
                awnser.config(text = d)
    else:
        d = list(jeffsayings)[0]
        awnser.config(text = d)


    


#window set up / settings
root = tk.Tk()
root.title("JeffDoesMath")
root.geometry("200x300")

#widgits being created
exitb = tk.Button(root, command = leave, text = "exit")
entrybox = tk.Entry(root, width = 15,)
solvebutton = tk.Button(root, command = solve, text = "solve")
awnser = tk.Label(root, text = list(jeffsayings)[0])

#add widget to windows :3
exitb.place(x=175, y=250)
entrybox.place(x= 0, y=250)
solvebutton.place(x=0, y=275)
awnser.place(x=0, y=200)



root.mainloop()

