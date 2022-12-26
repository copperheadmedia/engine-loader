import tkinter as tk
import config
import os

window = tk.Tk()

window.title("engine loader")

os.remove('engine-simulator/engine-sim-build_0_1_11a/assets/main.mr')

def write_mods(file_name, folder_name):
    line1 = "import \"engine_sim.mr\""
    line2 = "import \"themes/default.mr\""
    line5 = "use_default_theme()"
    line6 = "main()"

    with open('engine-simulator/engine-sim-build_0_1_11a/assets/main.mr', 'w') as f:
        f.write(line1)
        f.write(line2)
        f.write("\n")
        f.write(f"import \"engines/{folder_name}/{file_name}\"")
        f.write(line5)
        f.write(line6)

for i in range(len(config.engine_name)):
    button = tk.Button(window, text=f"{config.engine_name[i]}",height=3, font=('Arial', 16), command=write_mods(config.file_name,config.folder_name))
    button.pack()


window.mainloop()