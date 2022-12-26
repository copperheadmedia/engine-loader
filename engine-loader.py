import tkinter as tk
import config
import os

window = tk.Tk()

window.title("engine loader")

os.remove('engine_simulator/engine-sim-build_0_1_11a/assets/main.mr')

def write_mods(file_name, folder_name):
    with open('engine_simulator/engine-sim-build_0_1_11a/assets/main.mr', 'w') as f:
        f.write("import \"engine_sim.mr\"\n")
        f.write("import \"themes/default.mr\"\n")
        f.write(f"import \"engines/{folder_name}/{file_name}\"\n")
        f.write("\n")
        f.write("use_default_theme()\n")
        f.write("main()\n")
    os.startfile("engine_simulator/engine-sim-build_0_1_11a/bin/engine-sim-app.exe")

for i in range(len(config.engine_name)):
    button = tk.Button(window, text=f"{config.engine_name[i]}",height=3, font=('Arial', 16), command=write_mods(config.file_name,config.folder_name))
    button.pack()


window.mainloop()