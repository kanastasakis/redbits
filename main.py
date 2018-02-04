import Tkinter as tk
from redbits import Application

root = tk.Tk()
app = Application(master=root)
app.mainloop()

try:
    # TODO: Using the exit button causes and error. Why>
    root.destroy()
except:
    pass