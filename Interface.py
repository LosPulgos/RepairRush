import customtkinter as ctk
import sound_manager as sm
import time
import threading

# Configuration de base du mode sombre
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Instanciation de SoundManager
sound_manager = sm.SoundManager()

# Son de la caisse
def play_sound():
    sound_manager.playsound('./sounds/ca-ching.mp3')  # Remplace par le chemin correct de ton fichier son

# Créer la fenêtre principale
root = ctk.CTk()
root.title("Repair Rush")
root.geometry("1280x720")  # Fenêtre plus grande

# Variable pour savoir quel menu (machine ou technicien) était ouvert avant d'ouvrir les paramètres
menu_ouvert = None

# Profil du joueur (élargi pour correspondre à la barre de progression)
profile_frame = ctk.CTkFrame(root, width=600, height=150, corner_radius=10, fg_color="#FFA500")
profile_frame.place(x=10, y=10)

# Utiliser `place` pour organiser les éléments du profil
profile_label = ctk.CTkLabel(profile_frame, text="Mr Boss", font=("Arial", 16), text_color="black")
profile_label.place(x=10, y=10)

role_label = ctk.CTkLabel(profile_frame, text="Boss International", font=("Arial", 10), text_color="black")
role_label.place(x=10, y=40)

info_label = ctk.CTkLabel(profile_frame, text="Jour actuel\nArgent actuel\nRevenus par période\nCoûts fixes\nSolde net",
                          font=("Arial", 10), text_color="black")
info_label.place(x=10, y=70)

# Barre de progression (Revenus toutes les 30 secondes)
progress_bar = ctk.CTkProgressBar(root, width=600, height=30, progress_color='green')
progress_bar.place(x=10, y=170)

# Fonction pour mettre à jour la barre de progression
def update_progress_bar():
    while True:
        for i in range(3001):  # 31 étapes pour 30 secondes
            progress_bar.set(i / 3000)  # Met à jour la barre (0 à 1)
            time.sleep(0.01)
        play_sound()  # Joue le son à la fin des 30 secondes
        progress_bar.set(0)

# Lancer la barre de progression dans un thread séparé
def start_progress():
    threading.Thread(target=update_progress_bar, daemon=True).start()

# Conteneur scrollable pour afficher les machines ou les techniciens
scrollable_frame = ctk.CTkScrollableFrame(root, width=600, height=300, fg_color="#FF7F7F")
scrollable_frame.place(x=650, y=100)

# Fonction pour afficher les machines
def afficher_machines():
    global menu_ouvert
    menu_ouvert = 'machines'
    
    # Effacer les éléments précédents
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Ajouter les informations des machines
    machine_info = [
        {"Nom": "Machine 1", "Durée": "5 sec", "Apport": "$100", "Type": "X"},
        {"Nom": "Machine 2", "Durée": "10 sec", "Apport": "$200", "Type": "X"},
        {"Nom": "Machine 3", "Durée": "15 sec", "Apport": "$300", "Type": "X"},
        {"Nom": "Machine 4", "Durée": "20 sec", "Apport": "$400", "Type": "X"},
        {"Nom": "Machine 5", "Durée": "25 sec", "Apport": "$500", "Type": "X"}
    ]

    for i, machine in enumerate(machine_info):
        machine_label = ctk.CTkLabel(scrollable_frame, text=f"{machine['Nom']} - {machine['Durée']} - {machine['Apport']} - {machine['Type']}")
        machine_label.grid(row=i, column=0, padx=10, pady=5, sticky="ew")

        # Bouton d'achat pour chaque machine
        buy_button = ctk.CTkButton(scrollable_frame, text="Acheter", width=100)
        buy_button.grid(row=i, column=1, padx=10, pady=5)

# Fonction pour afficher les techniciens
def afficher_techniciens():
    global menu_ouvert
    menu_ouvert = 'techniciens'
    
    # Effacer les éléments précédents
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Ajouter les informations des techniciens
    technician_info = [
        {"Nom": "Technicien 1", "Spécialité": "Mécanique", "Durée": "5 sec", "Salaire": "$100"},
        {"Nom": "Technicien 2", "Spécialité": "Électrique", "Durée": "10 sec", "Salaire": "$200"},
        {"Nom": "Technicien 3", "Spécialité": "Informatique", "Durée": "15 sec", "Salaire": "$300"},
        {"Nom": "Technicien 4", "Spécialité": "Mécanique", "Durée": "20 sec", "Salaire": "$400"},
        {"Nom": "Technicien 5", "Spécialité": "Électrique", "Durée": "25 sec", "Salaire": "$500"}
    ]

    for i, technician in enumerate(technician_info):
        technician_label = ctk.CTkLabel(scrollable_frame, text=f"{technician['Nom']} - {technician['Spécialité']} - {technician['Durée']} - {technician['Salaire']}")
        technician_label.grid(row=i, column=0, padx=10, pady=5, sticky="ew")

        # Bouton d'engagement pour chaque technicien
        hire_button = ctk.CTkButton(scrollable_frame, text="Engager", width=100)
        hire_button.grid(row=i, column=1, padx=10, pady=5)

# Boutons des Machines et Techniciens
btn_machine = ctk.CTkButton(root, text="Btn Machine", width=140, height=50, command=afficher_machines)
btn_machine.place(x=650, y=20)

btn_technicien = ctk.CTkButton(root, text="Btn Technicien", width=140, height=50, command=afficher_techniciens)
btn_technicien.place(x=800, y=20)

# -- OPTIONS BUTTON AND OPTIONS MENU FUNCTIONALITY --

# Functions for the "Partie", "Son", and "Profil" sections
def open_partie():
    options_frame.lift()
    partie_button.configure(fg_color="gray")
    son_button.configure(fg_color="#FFA500")
    profil_button.configure(fg_color="#FFA500")
    # Show "Partie" section
    save_button.place(x=100, y=100)
    load_button.place(x=100, y=160)
    reset_button.place(x=100, y=220)
    # Hide other sections
    music_label.place_forget()
    music_slider.place_forget()
    effects_label.place_forget()
    effects_slider.place_forget()
    name_label.place_forget()
    name_entry.place_forget()
    currency_label.place_forget()
    currency_dropdown.place_forget()

def open_son():
    options_frame.lift()
    partie_button.configure(fg_color="#FFA500")
    son_button.configure(fg_color="gray")
    profil_button.configure(fg_color="#FFA500")
    # Show "Son" section
    music_label.place(x=350, y=100)
    music_slider.place(x=350, y=140)
    effects_label.place(x=350, y=180)
    effects_slider.place(x=350, y=220)
    # Hide other sections
    save_button.place_forget()
    load_button.place_forget()
    reset_button.place_forget()
    name_label.place_forget()
    name_entry.place_forget()
    currency_label.place_forget()
    currency_dropdown.place_forget()

def open_profil():
    options_frame.lift()
    partie_button.configure(fg_color="#FFA500")
    son_button.configure(fg_color="#FFA500")
    profil_button.configure(fg_color="gray")
    # Show "Profil" section
    name_label.place(x=600, y=100)
    name_entry.place(x=600, y=140)
    currency_label.place(x=600, y=180)
    currency_dropdown.place(x=600, y=220)
    # Hide other sections
    save_button.place_forget()
    load_button.place_forget()
    reset_button.place_forget()
    music_label.place_forget()
    music_slider.place_forget()
    effects_label.place_forget()
    effects_slider.place_forget()

# Function to hide the main game interface
def hide_game_interface():
    profile_frame.place_forget()
    progress_bar.place_forget()
    scrollable_frame.place_forget()
    btn_machine.place_forget()
    btn_technicien.place_forget()
    options_button.place_forget()
    options_frame.place(x=0, y=0)  # Display the options menu

# Function to show the main game interface
def show_game_interface():
    profile_frame.place(x=10, y=10)
    progress_bar.place(x=10, y=170)
    btn_machine.place(x=650, y=20)
    btn_technicien.place(x=800, y=20)
    options_button.place(x=950, y=20)
    options_frame.place_forget()  # Hide the options menu

    # Restaurer le menu précédemment ouvert (machines ou techniciens)
    if menu_ouvert == 'machines':
        scrollable_frame.place(x=650, y=100)
        afficher_machines()
    elif menu_ouvert == 'techniciens':
        scrollable_frame.place(x=650, y=100)
        afficher_techniciens()

# Button to open the options menu
options_button = ctk.CTkButton(root, text="⚙️", width=50, height=50, command=hide_game_interface)
options_button.place(x=950, y=20)

# Options frame (covers the entire window)
options_frame = ctk.CTkFrame(root, width=1280, height=720, fg_color="#E8C36A")
options_frame.place_forget()  # Initially hidden

# Buttons for the "Partie", "Son", and "Profil" sections
partie_button = ctk.CTkButton(options_frame, text="Partie", width=200, command=open_partie)
son_button = ctk.CTkButton(options_frame, text="Son", width=200, command=open_son)
profil_button = ctk.CTkButton(options_frame, text="Profil", width=200, command=open_profil)

# Positioning the buttons
partie_button.place(x=100, y=20)
son_button.place(x=350, y=20)
profil_button.place(x=600, y=20)

# "Partie" section elements
save_button = ctk.CTkButton(options_frame, text="Sauvegarder")
load_button = ctk.CTkButton(options_frame, text="Charger une partie")
reset_button = ctk.CTkButton(options_frame, text="Réinitialiser la partie")

# "Son" section elements
music_label = ctk.CTkLabel(options_frame, text="Musique")
music_slider = ctk.CTkSlider(options_frame)
effects_label = ctk.CTkLabel(options_frame, text="Effets Sonores")
effects_slider = ctk.CTkSlider(options_frame)

# "Profil" section elements
name_label = ctk.CTkLabel(options_frame, text="Nom:")
name_entry = ctk.CTkEntry(options_frame)
currency_label = ctk.CTkLabel(options_frame, text="Monnaie:")
currency_dropdown = ctk.CTkComboBox(options_frame, values=["€", "$", "£"])

# Function to close the options menu and return to the game interface
def close_options():
    show_game_interface()

# Button to return to the game from options menu
back_button = ctk.CTkButton(options_frame, text="←", width=50, command=close_options)
back_button.place(x=1200, y=20)

# Démarrer la barre de progression dès le début
start_progress()

# Boucle principale de l'application
root.mainloop()
