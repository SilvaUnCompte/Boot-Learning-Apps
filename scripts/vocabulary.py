import os
import random
import tkinter as tk
import pandas as pd
from tkinter import ttk

nb_word = 6
current_dir = os.path.dirname(os.path.abspath(__file__))

# Chargement du vocabulaire depuis un CSV
def load_vocab(filename):

    df = pd.read_excel(os.path.join(current_dir, filename))

    # Parcours chaque ligne et vérifie le nombre de colonnes non vides
    for i, row in df.iterrows():
        # On compte les colonnes non nulles dans la ligne
        non_null_cols = row.dropna()
        if len(non_null_cols) != 2:
            print(f"Ligne {i+2} mal formée : {row.values}")  # i+2 car Excel commence à 1 et on a l'en-tête

    # Si tu veux voir toutes les lignes valides :
    valide = df.dropna(thresh=2)  # garde lignes avec au moins 2 valeurs non nulles
    print(f"Lignes valides : {len(valide)}")
    return valide

# Liste des paires (mot, définition)
vocab_list = load_vocab("vocabulaire.xlsx")
selected_vocab = []

# Interface tkinter
root = tk.Tk()
root.title("Révision Vocabulaire")
root.geometry("1200x400")

# Variables tkinter
vocab_vars = [tk.StringVar() for _ in range(nb_word)]
answer_vars = [tk.StringVar() for _ in range(nb_word)]

# Fonction de génération
def generate():
    global selected_vocab
    selected_vocab = random.sample(list(vocab_list.itertuples(index=False, name=None)), nb_word)
    for i in range(nb_word):
        vocab_vars[i].set(f"Mot {i+1} : {selected_vocab[i][0]}")
        answer_vars[i].set("")

# Fonction d'affichage des définitions
def show_answer(index):
    answer_vars[index].set(f"Définition : {selected_vocab[index][1]}")

# Layout de l'interface
frame = ttk.Frame(root, padding=10)
frame.pack()

for i in range(nb_word):
    ttk.Label(frame, textvariable=vocab_vars[i], font=("Arial", 12)).grid(row=i, column=0, sticky="w", padx=5)
    ttk.Button(frame, text="Answer", command=lambda idx=i: show_answer(idx)).grid(row=i, column=1, padx=5)
    ttk.Label(frame, textvariable=answer_vars[i], font=("Arial", 12), foreground="blue").grid(row=i, column=2, sticky="w")

# Bouton Generate
ttk.Button(root, text="Generate", command=generate).pack(pady=10)

# Lancement initial
generate()
root.mainloop()
