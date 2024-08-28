import tkinter as tk

class ContCreciente:
    def __init__(self, master):
        self.master = master
        self.master.title("ContCreciente")
        self.master.geometry("300x200")
        self.master.config(bg="#f0f0f0")
        self.counter = 0
        self.label = tk.Label(text="Contador", font=("Arial", 24), bg="#f0f0f0")
        self.label.pack(pady=10)
        self.entry = tk.Entry(width=10, font=("Arial", 24), justify="center")
        self.entry.insert(0, "0")
        self.entry.config(state="readonly")
        self.entry.pack(pady=10)
        self.button = tk.Button(text="+", command=self.boton_incrementar, font=("Arial", 24), bg="#4CAF50", fg="#ffffff")
        self.button.pack(pady=10)

    def boton_incrementar(self):
        self.counter += 1
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.counter))
        self.entry.config(state="readonly")

root = tk.Tk()
app = ContCreciente(root)
root.mainloop()