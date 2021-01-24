import tkinter as tk 

root = tk.Tk()

tk.Button(root,text='Absolute Positioning').place(x = 20,y = 10)
tk.Button(root,text='Relative Positioning').place(relx = 0.8,rely = 0.2,relwidth=0.5,width=10,anchor=tk.NE) # Anchor defines relative to what

root.mainloop()