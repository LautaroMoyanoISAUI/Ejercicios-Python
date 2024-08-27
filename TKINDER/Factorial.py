import tkinter as tk

class Factorial:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Factorial - [Preview]")
        self.master.geometry("600x150")
        self.master.config(bg="#f0f0f0")
        self.n = 1
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)
        self.label_n = tk.Label(self.frame, text="n", font=("Arial", 14), bg="#f0f0f0")
        self.label_n.grid(row=0, column=0, padx=10, pady=10)
        self.entry_n = tk.Entry(self.frame, width=10, font=("Arial", 14), justify="center")
        self.entry_n.insert(0, str(self.n))
        self.entry_n.config(state="readonly")
        self.entry_n.grid(row=0, column=1, padx=10, pady=10)
        self.label_factorial = tk.Label(self.frame, text="Factorial (n)", font=("Arial", 14), bg="#f0f0f0")
        self.label_factorial.grid(row=0, column=2, padx=10, pady=10)
        self.entry_factorial = tk.Entry(self.frame, width=10, font=("Arial", 14), justify="center")
        self.entry_factorial.config(state="readonly")
        self.entry_factorial.grid(row=0, column=3, padx=10, pady=10)
        self.button_siguiente = tk.Button(self.frame, text="Siguiente", command=self.boton_siguiente, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_siguiente.grid(row=1, column=2, columnspan=2, padx=10, pady=10)


    def boton_siguiente(self):
        self.n += 1
        self.entry_n.config(state="normal")
        self.entry_n.delete(0, tk.END)
        self.entry_n.insert(0, str(self.n))
        self.entry_n.config(state="readonly")

        factorial = 1
        for i in range(1, self.n + 1):
            factorial *= i

        self.entry_factorial.config(state="normal")
        self.entry_factorial.delete(0, tk.END)
        self.entry_factorial.insert(0, str(factorial))
        self.entry_factorial.config(state="readonly")

root = tk.Tk()
app = Factorial(root)
root.mainloop()