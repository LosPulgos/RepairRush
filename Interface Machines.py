import tkinter as tk
from tkinter import Canvas

class InterfaceGraphique:
    def __init__(self, root, machines):
        self.root = root
        self.root.title("État des Machines")
        self.machines = machines
        self.create_interface()

    def create_interface(self):
        # Canvas pour dessiner les machines et les barres d'état
        canvas = Canvas(self.root, width=600, height=200, bg='lightgreen')
        canvas.pack()

        x_position = 50  # Position de départ pour la première machine

        for machine in self.machines:
            # Dessiner une "machine" (remplace avec une image si nécessaire)
            canvas.create_rectangle(x_position, 50, x_position + 50, 100, fill="black")
            
            # Créer une barre d'état basée sur l'état de la machine
            etat_color = self.get_color_for_etat(machine.etat)
            canvas.create_rectangle(x_position + 60, 50, x_position + 80, 50 + (machine.etat / 2), fill=etat_color)
            
            # Mettre à jour la position x pour la prochaine machine
            x_position += 100
    
    def get_color_for_etat(self, etat):
        # Retourne une couleur en fonction de l'état de la machine
        if etat >= 70:
            return "green"
        elif 30 <= etat < 70:
            return "yellow"
        else:
            return "red"

# Exemple de classe Machine avec un état
class Machine:
    def __init__(self, nom, etat):
        self.nom = nom
        self.etat = etat

# Création de quelques machines pour l'exemple
machines = [
    Machine("Tour", 90),
    Machine("Tour Avancé", 80),
    Machine("Fraiseuse", 60),
    Machine("Fraiseuse Avancée", 40),
    Machine("Perceuse", 20),
    Machine("Perceuse Avancée", 75)
]

# Créer l'interface Tkinter
root = tk.Tk()
interface = InterfaceGraphique(root, machines)
root.mainloop()
