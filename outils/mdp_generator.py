import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Génération du mot de passe ---
def generer_mdp():
    longueur = longueur_var.get()
    charset = ""
    if minuscule_var.get():
        charset += string.ascii_lowercase
    if majuscule_var.get():
        charset += string.ascii_uppercase
    if chiffres_var.get():
        charset += string.digits
    if symboles_var.get():
        charset += string.punctuation
    if not charset:
        messagebox.showwarning("Alerte", "Choisis au moins un type de caractère.")
        return
    mot_de_passe = ''.join(random.choice(charset) for _ in range(longueur))
    resultat_var.set(mot_de_passe)

def copier_mdp():
    mdp = resultat_var.get()
    if mdp:
        root.clipboard_clear()
        root.clipboard_append(mdp)
        messagebox.showinfo("Succès", "Mot de passe copié.")

# --- Couleurs et Polices ---
BG = "#0f1117"
CARD = "#1f222d"
BTN = "#3b82f6"
BTN_HOVER = "#2563eb"
TEXT = "#e2e8f0"
ACCENT = "#f472b6"
FONT_BIG = ("Segoe UI", 22, "bold")
FONT_TXT = ("Segoe UI", 14)
FONT_BTN = ("Segoe UI", 13, "bold")

# --- Fenêtre principale ---
root = tk.Tk()
root.title("🔐 Générateur sécurisé")
root.geometry("480x540")
root.configure(bg=BG)
root.resizable(False, False)

# --- Cadre central ---
card = tk.Frame(root, bg=CARD, bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=480)

tk.Label(card, text="🔐 Générateur de mot de passe", font=FONT_BIG, bg=CARD, fg=ACCENT).pack(pady=20)

# --- Variables ---
longueur_var = tk.IntVar(value=16)
minuscule_var = tk.BooleanVar(value=True)
majuscule_var = tk.BooleanVar(value=True)
chiffres_var = tk.BooleanVar(value=True)
symboles_var = tk.BooleanVar(value=True)
resultat_var = tk.StringVar()

# --- Fonctions Interface ---
def create_label(text):
    return tk.Label(card, text=text, font=FONT_TXT, bg=CARD, fg=TEXT)

def create_check(text, var):
    return tk.Checkbutton(card, text=text, variable=var, font=FONT_TXT, bg=CARD,
                          fg=TEXT, selectcolor=CARD, activebackground=CARD,
                          activeforeground=TEXT, anchor="w")

def hover_effect(btn):
    def on_enter(e): btn.config(bg=BTN_HOVER)
    def on_leave(e): btn.config(bg=BTN)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

def create_button(text, command, emoji=""):
    btn = tk.Button(card, text=f"{emoji} {text}", font=FONT_BTN, bg=BTN, fg="white",
                    activebackground=BTN_HOVER, relief="flat", bd=0,
                    command=command, padx=12, pady=8, highlightthickness=0)
    hover_effect(btn)
    return btn

# --- Interface ---
create_label("Longueur du mot de passe :").pack()
tk.Spinbox(card, from_=4, to=64, textvariable=longueur_var, font=FONT_TXT, width=6,
           bg="#2e303e", fg="white", relief="flat", justify="center").pack(pady=5)

create_check("Minuscules (a-z)", minuscule_var).pack(anchor="w", padx=35)
create_check("Majuscules (A-Z)", majuscule_var).pack(anchor="w", padx=35)
create_check("Chiffres (0-9)", chiffres_var).pack(anchor="w", padx=35)
create_check("Symboles (!@#)", symboles_var).pack(anchor="w", padx=35)

create_button("Générer", generer_mdp, "⚙️").pack(pady=18)

entry = tk.Entry(card, textvariable=resultat_var, font=("Consolas", 16), justify="center",
                 state="readonly", bg="#2e303e", fg=ACCENT, relief="flat")
entry.pack(pady=6, padx=25, fill="x")
entry.config(highlightthickness=1, highlightbackground=ACCENT)

create_button("Copier", copier_mdp, "📋").pack(pady=14)

# --- Crédit ---
tk.Label(root, text="by ton nom ici", bg=BG, fg="#6b7280", font=("Segoe UI", 10)).pack(side="bottom", pady=6)

root.mainloop()
