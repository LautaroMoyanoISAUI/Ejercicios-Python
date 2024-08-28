import tkinter as tk
from random import randint

class GeneradorNumeros:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de números")
        label1 = tk.Label(self.root, text="Número 1")
        label1.grid(row=0, column=0)
        label2 = tk.Label(self.root, text="Número 2")
        label2.grid(row=1, column=0)
        label3 = tk.Label(self.root, text="Número Generado")
        label3.grid(row=2, column=0)
        self.spinBox1 = tk.Spinbox(self.root, from_=1, to=100)
        self.spinBox1.grid(row=0, column=1)
        self.spinBox2 = tk.Spinbox(self.root, from_=1, to=100)
        self.spinBox2.grid(row=1, column=1)
        self.lineEdit = tk.Entry(self.root, state="readonly")
        self.lineEdit.grid(row=2, column=1)
        button = tk.Button(self.root, text="Generar", command=self.generarNumero)
        button.grid(row=3, column=0, columnspan=2)
    def generarNumero(self):
        num1 = int(self.spinBox1.get())
        num2 = int(self.spinBox2.get())
        numero_generado = randint(num1, num2)
        self.lineEdit.config(state="normal")
        self.lineEdit.delete(0, tk.END)
        self.lineEdit.insert(0, str(numero_generado))
        self.lineEdit.config(state="readonly")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = GeneradorNumeros()
    app.run()