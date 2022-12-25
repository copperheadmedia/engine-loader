import tkinter as tk
import json

config = open("config.json")

data = json.load(config)

window = tk.Tk()

window.mainloop()