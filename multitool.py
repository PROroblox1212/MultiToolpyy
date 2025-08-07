import tkinter as tk
import subprocess
import update

def ouvrir_mdp_manager():
    subprocess.Popen(["python", "outils/mdp_manager.py"])

def lancer_mise_a_jour():
    update.update()

root = tk.Tk()
root.title("MultiTool")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Outils disponibles", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Gestionnaire de mots de passe", command=ouvrir_mdp_manager).pack(pady=5)
tk.Button(root, text="🔄 Mettre à jour", fg="white", bg="green", command=lancer_mise_a_jour).pack(pady=10)

root.mainloop()
