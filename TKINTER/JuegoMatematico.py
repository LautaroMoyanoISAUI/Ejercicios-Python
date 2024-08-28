import tkinter as tk
from random import randint, choice
class JuegoMatematico:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x250")
        self.master.title("Juego Matematico")
        self.master.resizable(False, False)

        self.label_juegos = tk.Label(self.master, text="Juegos:")
        self.label_juegos.grid(row=4, column=5, padx=5, pady=5)

        self.label_buenos = tk.Label(self.master, text="Buenos:")
        self.label_buenos.grid(row=5, column=5, padx=5, pady=5)

        self.label_malos = tk.Label(self.master, text="Malos:")
        self.label_malos.grid(row=6, column=5, padx=5, pady=5)

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

    def nuevo_juego(self):
        self.num1 = randint(1, 10)
        self.num2 = randint(1, 10)
        self.operacion_random = choice(["+", "-", "*", "/"])

        self.label_num1.config(text=str(self.num1))
        self.label_num2.config(text=str(self.num2))
        self.label_operacion.config(text=self.operacion_random)

        self.entry_resultado.delete(0, tk.END)

    def verificar_resultado(self):
        resultado = self.entry_resultado.get()
        if resultado == "":
            return

        resultado = float(resultado)

        if self.operacion_random == "+":
            resultado_correcto = self.num1 + self.num2
        elif self.operacion_random == "-":
            resultado_correcto = self.num1 - self.num2
        elif self.operacion_random == "*":
            resultado_correcto = self.num1 * self.num2
        elif self.operacion_random == "/":
            resultado_correcto = self.num1 / self.num2
        if resultado == resultado_correcto:
            self.buenos += 1
            self.label_buenos.config(text="Buenos: " + str(self.buenos))
        else:
            self.malos += 1
            self.label_malos.config(text="Malos: " + str(self.malos))

        self.juegos += 1
        self.label_juegos.config(text="Juegos: " + str(self.juegos))

    def run(self):
        self.master.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoMatematico(root)
    juego.run()