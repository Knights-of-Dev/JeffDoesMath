import tkinter as tk
import random
import math
#functions

dumbness = 20

jeffsayings = {"mrrrrrp", "grrrrrr", "murp", "gurp", "RAWR", "MRRRRRRRRRf", "BLAARGGULARG", "AHHHHbabababababa", "eaaaarrrgghhh", "*shows Ming the Cowculator at https://github.com/Knights-of-Dev/Ming-the-Cowculator*", "glup", "yes math", "no math", "deadpool fren", "gwenpool fren", "I avenger", "grrrr", "I AM VENOMMMMMM", "Mrumph?", "Yip!", "Chomp-chomp!", "Mreeeeeee!", "Murp-murp?", "prrrrrrrrr", "Stomp Stomp"}

chanceofmess = 10

def error():
    pass

def leave():
    root.destroy()


def settings():
    global dumbness
    global chanceofmess

    def apply():
        global dumbness
        global chanceofmess
        global dumbnessent
        global chanceofmessent
        dumbness = dumbnessent.get()
        chanceofmess = chanceofmessent.get()
        setwin.destroy()

    setwin = tk.Toplevel(root)
    setwin.title("JeffDoesMath-Settings")
    setwin.geometry("200x200")

    applybutton = tk.Button(setwin, text = "apply", command = apply)
    dumbnessentlabel = tk.Label(setwin, text = "dumbness")
    dumbnessent = tk.Entry(setwin, width = 5)
    chanceofmessentlabel = tk.Label(setwin, text = "chance of mess")
    chanceofmessent = tk.Entry(setwin, width = 5)

    applybutton.place(x=175,y=175)
    dumbnessentlabel.place(x=0,y=25)
    dumbnessent.place(x=0,y=50)
    chanceofmessentlabel.place(x=0,y=100)
    chanceofmessent.place(x=0,y=125)

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
    global chanceofmess
    global jeffsayings
    x = entrybox.get()
    x = x.split()
    if x[0] == "r" or x[0] == "R":
        a = int(x[1])
        a = math.radians(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "d" or x[0] == "D":
        a = int(x[1])
        a = math.degrees(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "√" or x[0] == "sqrt":
        a = int(x[1])
        a = math.sqrt(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "3√" or x[0] == "cbrt":
        a = int(x[1])
        a = math.cbrt(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "^" or x[0] == "pow":
        a = int(x[1])
        b = int(x[2])
        s = math.pow(a, b)
        if random.randint(1,chanceofmess) == 1:
            s =  messup(s)
        awnser.config(text = s)
    elif x[0] == "sin":
        a = int(x[1])
        a = math.sin(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "cos":
        a = int(x[1])
        a = math.cos(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "tan":
        a = int(x[1])
        a = math.tan(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "asin" or x[0] == "arcsin":
        a = int(x[1])
        a = math.asin(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "acos" or x[0] == "arccos":
        a = int(x[1])
        a = math.acos(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    elif x[0] == "atan" or x[0] == "arctan":
        a = int(x[1])
        a = math.atan(a)
        if random.randint(1,chanceofmess) == 1:
            a =  messup(a)
        awnser.config(text = a)
    else:
        if len(x) == 3:
            if x[0] == "pi":
                a = math.pi
            else:
                a = int(x[0])
                
            s = x[1]
            
            if x[2] == "pi":
                b = math.pi
            else:
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
                isdumb = random.randint(1,chanceofmess)
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
root.iconbitmap("icon.ico")

#widgits being created
exitb = tk.Button(root, command = leave, text = "exit")
entrybox = tk.Entry(root, width = 15,)
solvebutton = tk.Button(root, command = solve, text = "solve")
awnser = tk.Label(root, text = list(jeffsayings)[0])
settingsbutton = tk.Button(root, command = settings, text = "settings")

#add widget to windows :3
exitb.place(x=175, y=250)
settingsbutton.place(x=175, y=225)
entrybox.place(x= 0, y=250)
solvebutton.place(x=0, y=275)
awnser.place(x=0, y=200)



root.mainloop()

