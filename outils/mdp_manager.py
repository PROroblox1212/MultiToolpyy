import tkinter as tk
from tkinter import messagebox
import json
import os

FICHIER = "outils/passwords.json"

def charger_donnees():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r") as f:
            return json.load(f)
    return {}

def sauvegarder_donnees():
    with open(FICHIER, "w") as f:
        json.dump(donnees, f, indent=4)

def ajouter_mdp():
    site = entry_site.get()
    identifiant = entry_identifiant.get()
    mdp = entry_mdp.get()

    if not site or not identifiant or not mdp:
        messagebox.showwarning("Champs requis", "Remplis tous les champs.")
        return

    donnees[site] = {"identifiant": identifiant, "mdp": mdp}
    sauvegarder_donnees()
    mise_a_jour_liste()
    entry_site.delete(0, tk.END)
    entry_identifiant.delete(0, tk.END)
    entry_mdp.delete(0, tk.END)

def mise_a_jour_liste():
    liste_sites.delete(0, tk.END)
    for site in donnees:
        liste_sites.insert(tk.END, site)

def afficher_infos(event):
    selection = liste_sites.curselection()
    if selection:
        site = liste_sites.get(selection[0])
        infos = donnees[site]
        messagebox.showinfo(f"{site}", f"Identifiant: {infos['identifiant']}\nMot de passe: {infos['mdp']}")

def supprimer_site():
    selection = liste_sites.curselection()
    if selection:
        site = liste_sites.get(selection[0])
        if messagebox.askyesno("Confirmation", f"Supprimer {site} ?"):
            donnees.pop(site)
            sauvegarder_donnees()
            mise_a_jour_liste()

root = tk.Tk()
root.title("Gestionnaire de mots de passe")
root.geometry("350x400")

tk.Label(root, text="Site :").pack()
entry_site = tk.Entry(root)
entry_site.pack()

tk.Label(root, text="Identifiant :").pack()
entry_identifiant = tk.Entry(root)
entry_identifiant.pack()

tk.Label(root, text="Mot de passe :").pack()
entry_mdp = tk.Entry(root, show="*")
entry_mdp.pack()

tk.Button(root, text="Ajouter", command=ajouter_mdp).pack(pady=5)

tk.Label(root, text="Sites enregistrés :").pack()
liste_sites = tk.Listbox(root)
liste_sites.pack(fill=tk.BOTH, expand=True)
liste_sites.bind("<Double-Button-1>", afficher_infos)

tk.Button(root, text="Supprimer", command=supprimer_site).pack(pady=5)

donnees = charger_donnees()
mise_a_jour_liste()

root.mainloop()
