import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import randint

class TankLevelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nível do Tanque de Água")

        self.tank_level = tk.Label(root, text="Nível: ")
        self.tank_level.pack()

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        self.levels = []  # Lista para armazenar os níveis ao longo do tempo

        self.update_tank_level()

    def update_tank_level(self):
        level = randint(0, 100)  # Substitua por uma função que obtém o nível real do tanque
        self.levels.append(level)

        self.tank_level.config(text=f"Nível: {level}%")

        self.ax.clear()
        self.ax.plot(self.levels)
        self.ax.set_title("Evolução do Nível do Tanque")
        self.ax.set_xlabel("Tempo")
        self.ax.set_ylabel("Nível")
        self.canvas.draw()

        self.root.after(1000, self.update_tank_level)  # Atualiza a cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    app = TankLevelApp(root)
    root.mainloop()
