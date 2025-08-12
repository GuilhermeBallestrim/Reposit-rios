import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_user.get()
    password = entry_pass.get()
    # Exemplo de validação simples
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x180")

tk.Label(root, text="Usuário:").pack(pady=(20, 5))
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Senha:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Entrar", command=login).pack(pady=15)

root.mainloop()