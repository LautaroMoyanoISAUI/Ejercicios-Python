import tkinter as tk
from tkinter import ttk

class Peliculas:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Peliculas - [Preview]")
        self.master.geometry("700x300")
        self.master.config(bg="#f0f0f0")
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)
        self.label_titulo = tk.Label(self.frame, text="Escribe el título de una película", font=("Arial", 14), bg="#f0f0f0")
        self.label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.entry_titulo = tk.Entry(self.frame, width=30, font=("Arial", 14))
        self.entry_titulo.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.label_peliculas = tk.Label(self.frame, text="Peliculas", font=("Arial", 14), bg="#f0f0f0")
        self.label_peliculas.grid(row=0, column=2, padx=10, pady=10)
        self.listbox_peliculas = tk.Listbox(self.frame, width=30, height=5, font=("Arial", 14))
        self.listbox_peliculas.grid(row=1, column=2, padx=10, pady=10)
        self.button_añadir = tk.Button(self.frame, text="Añadir", command=self.añadir_pelicula, font=("Arial", 14), bg="#007bff", fg="#ffffff")
        self.button_añadir.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def añadir_pelicula(self):
        titulo = self.entry_titulo.get()
        if titulo:
            self.listbox_peliculas.insert(tk.END, titulo)
            self.entry_titulo.delete(0, tk.END)

root = tk.Tk()
app = Peliculas(root)
root.mainloop()
if __name__ == "__main__":
    peliculas = Peliculas()
    peliculas.run()