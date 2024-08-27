import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Calculadora")
        self.master.geometry("600x300")
        self.master.config(bg="#f0f0f0")
        self.label_num1 = tk.Label(self.master, text="Primer número", font=("Arial", 14), bg="#f0f0f0")
        self.label_num1.grid(row=0, column=0, padx=10, pady=10)
        self.label_num2 = tk.Label(self.master, text="Segundo número", font=("Arial", 14), bg="#f0f0f0")
        self.label_num2.grid(row=1, column=0, padx=10, pady=10)
        self.label_resultado = tk.Label(self.master, text="Resultado", font=("Arial", 14), bg="#f0f0f0")
        self.label_resultado.grid(row=2, column=0, padx=10, pady=10)
        self.entry_num1 = tk.Entry(self.master, width=20, font=("Arial", 14))
        self.entry_num1.grid(row=0, column=1, padx=10, pady=10)
        self.entry_num2 = tk.Entry(self.master, width=20, font=("Arial", 14))
        self.entry_num2.grid(row=1, column=1, padx=10, pady=10)
        self.entry_resultado = tk.Entry(self.master, width=20, font=("Arial", 14), state="readonly")
        self.entry_resultado.grid(row=2, column=1, padx=10, pady=10)
        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.button_suma = tk.Button(self.button_frame, text="+", command=lambda: self.operacion("+"), font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_suma.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_resta = tk.Button(self.button_frame, text="-", command=lambda: self.operacion("-"), font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_resta.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_multiplicacion = tk.Button(self.button_frame, text="*", command=lambda: self.operacion("*"), font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_multiplicacion.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_division = tk.Button(self.button_frame, text="/", command=lambda: self.operacion("/"), font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_division.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_porcentaje = tk.Button(self.button_frame, text="%", command=lambda: self.operacion("%"), font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_porcentaje.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_reset = tk.Button(self.button_frame, text="RESET", command=self.reset, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_reset.pack(side=tk.LEFT, padx=5, pady=5)

    def operacion(self, operador):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                resultado = num1 / num2
            elif operador == "%":
                resultado = num1 % num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, str(resultado))
            self.entry_resultado.config(state="readonly")
        except ValueError:
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, "Error")
            self.entry_resultado.config(state="readonly")

    def reset(self):
        self.entry_num1.delete(0, tk.END)
        self.entry_num2.delete(0, tk.END)
        self.entry_resultado.config(state="normal")
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.config(state="readonly")
root = tk.Tk()
my_calculator = Calculadora(root)
root.mainloop()