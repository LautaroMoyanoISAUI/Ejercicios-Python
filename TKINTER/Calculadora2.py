import tkinter as tk

class Calculadora2:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x250")
        self.master.title("calculadora")
        self.master.resizable(False, False)

        self.label_num1 = tk.Label(self.master, text='Primer Numero')
        self.label_num1.grid(row=0, column=0, padx=10, pady=10)

        self.label_num2 = tk.Label(self.master, text='Segundo Numero')
        self.label_num2.grid(row=1, column=0, padx=10, pady=10)

        self.label_num3 = tk.Label(self.master, text='Resultado')
        self.label_num3.grid(row=2, column=0, padx=10, pady=10)

        self.label_num4 = tk.Label(self.master, text='Operaciones')
        self.label_num4.grid(row=0, column=3, padx=10, pady=10)

        self.Entry_1_var = tk.StringVar(value=0)
        self.Entry_1 = tk.Entry(self.master, textvariable=self.Entry_1_var, justify="center")
        self.Entry_1.grid(row=0, column=2, padx=10, pady=10)
        

        self.Entry_2_var = tk.StringVar(value=0)
        self.Entry_2 = tk.Entry(self.master, textvariable=self.Entry_2_var, justify="center")
        self.Entry_2.grid(row=1, column=2, padx=10, pady=10)
        
        self.Entry_3_var = tk.StringVar(value=0)
        self.Entry_3 = tk.Entry(self.master, textvariable=self.Entry_3_var, state="readonly", justify="center")
        self.Entry_3.grid(row=2, column=2, padx=10, pady=10)

        self.opcion_var = tk.StringVar()
        self.opcion_var.set("sumar")

        self.rdbutton_1 = tk.Radiobutton(self.master, text='Sumar', variable=self.opcion_var, value="sumar")
        self.rdbutton_1.grid(row=1, column=3, padx=10, pady=10)

        self.rdbutton_2 = tk.Radiobutton(self.master, text='Restar', variable=self.opcion_var, value="resta")
        self.rdbutton_2.grid(row=2, column=3, padx=10, pady=10)
        self.rdbutton_3 = tk.Radiobutton(self.master, text='Multiplicar', variable=self.opcion_var, value="multiplicacion")
        self.rdbutton_3.grid(row=3, column=3, padx=10, pady=10)
        self.rdbutton_4 = tk.Radiobutton(self.master, text='Dividir', variable=self.opcion_var, value="division")
        self.rdbutton_4.grid(row=4, column=3, padx=10, pady=10)



        self.button_1 = tk.Button(self.master, text='Calcular', command=self.operacion)
        self.button_1.grid(row=4, column=2, padx=10, pady=10)


    def operacion(self):
        num1 = float(self.Entry_1_var.get())
        num2 = float(self.Entry_2_var.get())
        operacion = self.opcion_var.get()
        if operacion == "sumar":
            resultado = float(num1 + num2)
        elif operacion == "resta":
            resultado = float(num1 - num2)
        elif operacion == "multiplicacion":
            resultado = float(num1 * num2)
        elif operacion == "division":
            if num2 != 0:
                resultado = float(num1 / num2)
            else:
                resultado = "Error: Division por cero"
        self.Entry_3_var.set(resultado)

root = tk.Tk()
my_calculator = Calculadora2(root)
root.mainloop()