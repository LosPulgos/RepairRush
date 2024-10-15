# main.py

import customtkinter as ctk

# Initialisation 
app = ctk.CTk()
app.title("Repair Rush")
app.geometry("800x600")

# Fenêtre principale du jeu
def create_main_window():
    label = ctk.CTkLabel(app, text="Bienvenue dans Repair Rush")
    label.pack(pady=20)

create_main_window()

# Lancer l'app
app.mainloop()
