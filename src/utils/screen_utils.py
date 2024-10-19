import tkinter as tk

def get_screen_dimensions():
    root = tk.Tk()
    root.withdraw()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    root.destroy()
    return width, height