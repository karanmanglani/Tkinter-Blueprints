import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="I am a label widget")
button = tk.Button(root, text="I am a button")
label.pack()
button.pack()
tk.Label(root,text='Direct Addition into the application (Use only if you dont need to manipulate or retrieve data from this labal)').pack()
root.mainloop()
