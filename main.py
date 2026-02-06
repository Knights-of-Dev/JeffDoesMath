import tkinter as tk
#functions
def leave:
    root.destroy()




#window set up / settings
root = tk.Tk()
root.title("Basic tkinter set up :3")
root.geometry("300x200")

#widgits being created
exit = tk.Button(root, command = leave)


#add widget to windows :3
exit.grid(row= 3, column= 2)




root.mainloop()


