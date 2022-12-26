import tkinter as tk
import config

window = tk.Tk()

window.title("engine loader")

for i in range(len(config.engine_name)):
    button = tk.Button(window, text=f"{config.engine_name[i]}",height=3, font=('Arial', 16))
    button.pack()

window.mainloop()