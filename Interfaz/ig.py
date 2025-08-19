import tkinter as tk
from tkinter import messagebox, filedialog

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")
        #Crea area de texto
        self.text_area = tk.Text(self, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        #Crea barra de menu
        self.crear_menu()

    def crear_menu(self):
        menu_bar = tk.Menu(self)
        filemenu = tk.Menu(menu_bar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=filemenu)
        self.config(menu=menu_bar)
        
    def abrir_archivo(self):
        item = filedialog.askopenfilename(
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if not item:
            return
        try:
            with open(item, 'r', encoding='utf-8') as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
            
    def guardar_archivo(self):
        item = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if not item:
            return
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(item, 'w', encoding='utf-8') as file:
                file.write(contenido)
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()