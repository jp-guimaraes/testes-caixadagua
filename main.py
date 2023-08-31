import tkinter as tk
from random import randint

class TankLevelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nível do Tanque de Água")

        self.tank_level = tk.Label(root, text="Nível: ")
        self.tank_level.pack()

        self.update_tank_level()

    def update_tank_level(self):
        level = randint(0, 100)  # Substitua por uma função que obtém o nível real do tanque
        self.tank_level.config(text=f"Nível: {level}%")
        self.root.after(1000, self.update_tank_level)  # Atualiza a cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    app = TankLevelApp(root)
    root.mainloop()
