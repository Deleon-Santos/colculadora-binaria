"""Aplicação desenvolvida para facilitar o entendimento e ajudar nas atividades de matemática aplicada à computação"""

#Importação da biblioteca tkinter para a criação da interface gráfica
import tkinter as tk
from tkinter import messagebox


def binario_para_decimal():
    try:
        binario = entrada.get()
        valor_decimal = int(binario, 2)
        resultado.config(text=f"Resultado: {valor_decimal}")#conversão nativa do python
    except ValueError:
        messagebox.showerror("Erro", "Digite um número binário válido!")


def decimal_para_binario():
    try:
        decimal = int(entrada.get())
        resultado.config(text=f"Resultado: {bin(decimal)[2:]}")#conversão nativa do python
    except ValueError:
        messagebox.showerror("Erro", "Digite um número decimal válido!")


def hexadecimal_para_decimal():
    try:
        hexadecimal = entrada.get()
        valor_decimal = int(hexadecimal, 16)
        resultado.config(text=f"Resultado: {valor_decimal}")#conversão nativa do python
    except ValueError:
        messagebox.showerror("Erro", "Digite um número hexadecimal válido!")


def decimal_para_hexadecimal():
    try:
        decimal = int(entrada.get())
        resultado.config(text=f"Resultado: {hex(decimal)[2:]}")#conversão nativa do python
    except ValueError:
        messagebox.showerror("Erro", "Digite um número decimal válido!")


# Criando a interface grafica que devera deiixa o sistema mais intuitivp #

app = tk.Tk()
app.title("Calculadora Binária")
app.geometry("400x300")
app.resizable(False, False)

tk.Label(app, text="Valor de Entrada:", font=("Helvetica", 12)).pack(pady=5)

entrada = tk.Entry(app, font=("Helvetica", 15), justify="center")
entrada.pack(pady=5)

# Botões de operação alinhados
tk.Button(app, text="Binário → Decimal", width=25, command=binario_para_decimal).pack(pady=4)
tk.Button(app, text="Decimal → Binário", width=25, command=decimal_para_binario).pack(pady=4)
tk.Button(app, text="Hexadecimal → Decimal", width=25, command=hexadecimal_para_decimal).pack(pady=4)
tk.Button(app, text="Decimal → Hexadecimal", width=25, command=decimal_para_hexadecimal).pack(pady=4)

resultado = tk.Label(app, text="Resultado: ", font=("Arial", 12, "bold"))
resultado.pack(pady=10)

app.mainloop() #carrega a janela
