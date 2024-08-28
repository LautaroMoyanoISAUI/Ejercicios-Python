import tkinter as tk

class JuegoMatematico:
    def __init__(self):
        self.master = master
        self.master.geometry("400x250")
        self.master.title("Juego Matematico")
        self.master.resizable(False, False)

        self.label_juegos = tk.Label(self.master, text="Juegos:")
        self.label_juegos.grid(row=0, column=0, padx=10, pady=10)

        self.label_buenos = tk.Label(self.master, text="Buenos:")
        self.label_buenos.grid(row=0, column=2, padx=10, pady=10)

        self.label_malos = tk.Label(self.master, text="Malos:")
        self.label_malos.grid(row=0, column=4, padx=10, pady=10)

        self.label_num1 = tk.Label(self.master, text="")
        self.label_num1.grid(row=1, column=0, padx=10, pady=10)

        self.label_num2 = tk.Label(self.master, text="")
        self.label_num2.grid(row=1, column=2, padx=10, pady=10)

        self.label_operacion = tk.Label(self.master, text="?")
        self.label_operacion.grid(row=1, column=1, padx=10, pady=10)

        self.label_resultado = tk.Label(self.master, text="")
        self.label_resultado.grid(row=2, column=0, padx=10, pady=10)


        self.entry_resultado = tk.Entry(self.master)
        self.entry_resultado.grid(row=2, column=2, padx=10, pady=10)

        self.button_nuevo_juego = tk.Button(self.master, text="Nuevo Juego", command=self.nuevo_juego)
        self.button_nuevo_juego.grid(row=3, column=0, padx=10, pady=10)

        self.button_resultado = tk.Button(self.master, text="Resultado", command=self.verificar_resultado)
        self.button_resultado.grid(row=3, column=2, padx=10, pady=10)

        self.operacion = tk.StringVar()
        self.operacion.set("+")
        self.radio_sumar = tk.Radiobutton(self.master, text="Sumar", variable=self.operacion, value="+")
        self.radio_restar = tk.Radiobutton(self.master, text="Restar", variable=self.operacion, value="-")
        self.radio_multiplicar = tk.Radiobutton(self.master, text="Multiplicar", variable=self.operacion, value="*")
        self.radio_dividir = tk.Radiobutton(self.master, text="Dividir", variable=self.operacion, value="/")

        self.radio_sumar.grid(row=4, column=0, padx=10, pady=10)
        self.radio_restar.grid(row=4, column=1, padx=10, pady=10)
        self.radio_multiplicar.grid(row=4, column=2, padx=10, pady=10)
        self.radio_dividir.grid(row=4, column=3, padx=10, pady=10)

        self.juegos = 0
        self.buenos = 0
        self.malos = 0

        self.nuevo_juego()

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
        
