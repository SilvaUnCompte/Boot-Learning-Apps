import random
import tkinter as tk
from tkinter import ttk
from num2words import num2words

# Données
days_fr = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
days_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
             "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
months_en = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]

seasons_fr = ["Printemps", "Été", "Automne", "Hiver"]
seasons_en = ["Spring", "Summer", "Autumn", "Winter"]

# Variables globales
random_day_idx = random_month_idx = random_season_idx = hour = minute = number = 0

# Tkinter setup
root = tk.Tk()
root.title("Générateur Bilingue Aligné")
root.geometry("600x300")

# Variables tkinter
day_var = tk.StringVar()
month_var = tk.StringVar()
season_var = tk.StringVar()
time_var = tk.StringVar()
number_var = tk.StringVar()

# Fonction pour générer de nouvelles données
def generate():
    global random_day_idx, random_month_idx, random_season_idx, hour, minute, number
    random_day_idx = random.randint(0, 6)
    random_month_idx = random.randint(0, 11)
    random_season_idx = random.randint(0, 3)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    number = random.randint(10_000, 999_999)
    show_french()

# Fonctions d'affichage
def show_french():
    day_var.set(f"Jour : {days_fr[random_day_idx]}")
    month_var.set(f"Mois : {months_fr[random_month_idx]}")
    season_var.set(f"Saison : {seasons_fr[random_season_idx]}")

    # Calcul de l’heure arrondie à 5 min
    rounded_min = round(minute / 5) * 5
    local_hour = hour
    if rounded_min == 60:
        rounded_min = 0
        local_hour = (hour + 1) % 24

    time_var.set(f"Heure : {local_hour}h{rounded_min:02d}")
    number_var.set(f"Nombre : {number}")

# Fonctions de traduction
def translate_day():
    day_var.set(f"Day: {days_en[random_day_idx]}")

def translate_month():
    month_var.set(f"Month: {months_en[random_month_idx]}")

def translate_season():
    season_var.set(f"Season: {seasons_en[random_season_idx]}")

def translate_time():
    # Arrondi à 5 minutes les plus proches
    rounded_min = round(minute / 5) * 5
    local_hour = hour

    if rounded_min == 60:
        rounded_min = 0
        local_hour = (hour + 1) % 24

    if rounded_min == 0:
        time_str = f"{num2words(local_hour % 12 or 12, lang='en')} o'clock"
    elif rounded_min == 15:
        time_str = f"quarter past {num2words(local_hour % 12 or 12, lang='en')}"
    elif rounded_min == 30:
        time_str = f"half past {num2words(local_hour % 12 or 12, lang='en')}"
    elif rounded_min == 45:
        next_hour = (local_hour + 1) % 24
        time_str = f"quarter to {num2words(next_hour % 12 or 12, lang='en')}"
    elif rounded_min < 30:
        time_str = f"{num2words(rounded_min, lang='en')} past {num2words(local_hour % 12 or 12, lang='en')}"
    else:
        minutes_to = 60 - rounded_min
        next_hour = (local_hour + 1) % 24
        time_str = f"{num2words(minutes_to, lang='en')} to {num2words(next_hour % 12 or 12, lang='en')}"

    time_var.set(f"Time: {time_str}")

def translate_number():
    number_text = f"{num2words(number, lang='en')}"
    current = number_var.get()
    number_var.set(f"{current}\n{number_text}")

# Cadre principal
frame = ttk.Frame(root, padding=10)
frame.pack()

# Lignes avec éléments + boutons
ttk.Label(frame, textvariable=day_var, font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=5)
ttk.Button(frame, text="Answer", command=translate_day).grid(row=0, column=1, padx=5)

ttk.Label(frame, textvariable=month_var, font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5)
ttk.Button(frame, text="Answer", command=translate_month).grid(row=1, column=1, padx=5)

ttk.Label(frame, textvariable=season_var, font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5)
ttk.Button(frame, text="Answer", command=translate_season).grid(row=2, column=1, padx=5)

ttk.Label(frame, textvariable=time_var, font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5)
ttk.Button(frame, text="Answer", command=translate_time).grid(row=3, column=1, padx=5)

ttk.Label(frame, textvariable=number_var, font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5)
ttk.Button(frame, text="Answer", command=translate_number).grid(row=4, column=1, padx=5)

# Bouton Generate
ttk.Button(root, text="Generate", command=generate).pack(pady=10)

# Lancement initial
generate()

root.mainloop()