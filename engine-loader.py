import tkinter as tk
import json

config = open("config.json")
engine = open("engine.json")

data_config = json.load(config)
data_engine = json.load(engine)

window = tk.Tk()

window.mainloop()