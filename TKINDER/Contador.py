import tkinter as tk

class Contador:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Contador")
        self.master.geometry("600x150")
        self.master.config(bg="#f0f0f0")
        self.contador = 0
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)
        self.label_contador = tk.Label(self.frame, text="Contador", font=("Arial", 14), bg="#f0f0f0")
        self.label_contador.grid(row=0, column=0, padx=10, pady=10)
        self.entry_contador = tk.Entry(self.frame, width=10, font=("Arial", 14), justify="center")
        self.entry_contador.insert(0, str(self.contador))
        self.entry_contador.config(state="readonly")
        self.entry_contador.grid(row=0, column=1, padx=10, pady=10)
        self.button_up = tk.Button(self.frame, text="Count Up", command=self.boton_up, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_up.grid(row=1, column=0, padx=10, pady=10)
        self.button_down = tk.Button(self.frame, text="Count Down", command=self.boton_down, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_down.grid(row=1, column=1, padx=10, pady=10)
        self.button_reset = tk.Button(self.frame, text="Reset", command=self.boton_reset, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_reset.grid(row=1, column=2, padx=10, pady=10)

    def boton_up(self):
        self.contador += 1
        self.entry_contador.config(state="normal")
        self.entry_contador.delete(0, tk.END)
        self.entry_contador.insert(0, str(self.contador))
        self.entry_contador.config(state="readonly")

    def boton_down(self):
        self.contador -= 1
        self.entry_contador.config(state="normal")
        self.entry_contador.delete(0, tk.END)
        self.entry_contador.insert(0, str(self.contador))
        self.entry_contador.config(state="readonly")

    def boton_reset(self):
        self.contador = 0
        self.entry_contador.config(state="normal")
        self.entry_contador.delete(0, tk.END)
        self.entry_contador.insert(0, str(self.contador))
        self.entry_contador.config(state="readonly")

root = tk.Tk()
app = Contador(root)
root.mainloop()