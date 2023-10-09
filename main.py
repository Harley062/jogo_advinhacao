import tkinter as tk
from tkinter import messagebox

def verificar_chute():
    chute = int(chute_entry.get())
    
    if chute == numero_secreto:
        messagebox.showinfo("Resultado", "Parabéns! Você acertou o número.")
        root.quit()
    elif chute < numero_secreto:
        messagebox.showinfo("Resultado", "Tente um número maior.")
    else:
        messagebox.showinfo("Resultado", "Tente um número menor.")

root = tk.Tk()
root.title("Jogo de Adivinhação")

numero_secreto = 42

titulo_label = tk.Label(root, text="Bem-vindo ao Jogo de Adivinhação!")
titulo_label.pack(pady=10)

instrucao_label = tk.Label(root, text="Digite o seu número:")
instrucao_label.pack()

chute_entry = tk.Entry(root)
chute_entry.pack()

verificar_button = tk.Button(root, text="Verificar", command=verificar_chute)
verificar_button.pack(pady=10)

root.mainloop()
