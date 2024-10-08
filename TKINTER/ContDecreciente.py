import tkinter as tk

class ContDecreciente:
    def __init__(self, master):
        self.master = master
        self.master.title("ContDecreciente")
        self.master.geometry("300x200")
        self.master.config(bg="#f0f0f0")
        self.counter = 88
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)
        self.label = tk.Label(self.frame, text="Contador", font=("Arial", 24), bg="#f0f0f0")
        self.label.pack(pady=10)
        self.entry = tk.Entry(self.frame, width=10, font=("Arial", 24), justify="center")
        self.entry.insert(0, "88")
        self.entry.config(state="readonly")
        self.entry.pack(pady=10)
        self.button = tk.Button(self.frame, text="-", command=self.boton_decrementar, font=("Arial", 24), bg="#4CAF50", fg="#ffffff")
        self.button.pack(pady=10)

    def boton_decrementar(self):
        self.counter -= 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.counter))
        self.entry.config(state="readonly")

root = tk.Tk()
app = ContDecreciente(root)
root.mainloop()