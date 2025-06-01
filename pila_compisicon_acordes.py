import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class NotaTocada:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # "Nota" o "Acorde"
        self.timestamp = datetime.now().strftime("%H:%M:%S")
    
    def __str__(self):
        simbolo = "N" if self.tipo == "Nota" else "A"
        return f"[{simbolo}] {self.nombre} - {self.timestamp}"

class HistorialNotasGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Teclado Piano - Historial de Notas")
        self.ventana.geometry("700x600")
        
        self.historial = []

        # Área de historial (pila)
        tk.Label(self.ventana, text="Historial (pila de notas)", font=("Arial", 14, "bold")).pack(pady=5)
        self.texto_historial = tk.Text(self.ventana, height=10, state="disabled", bg="#f0f0f0")
        self.texto_historial.pack(padx=10, pady=5, fill="x")

        # Controles
        controles_frame = tk.Frame(self.ventana)
        controles_frame.pack(pady=5)
        tk.Button(controles_frame, text="Deshacer", command=self.deshacer_nota).pack(side="left", padx=5)
        tk.Button(controles_frame, text="Ver Última", command=self.ver_ultima).pack(side="left", padx=5)
        tk.Button(controles_frame, text="Limpiar", command=self.limpiar_historial).pack(side="left", padx=5)

        self.canvas = tk.Canvas(self.ventana, width=650, height=180, bg="white")
        self.canvas.pack(pady=10)
        
        self.crear_piano_rectangulos()
        self.ventana.mainloop()

    def crear_piano_rectangulos(self):
       
        self.teclas_blancas = ["C", "D", "E", "F", "G", "A", "B"]
        ancho_tecla = 80
        alto_tecla = 120
        
        for i, nota in enumerate(self.teclas_blancas):
            x1 = 50 + i * ancho_tecla
            y1 = 30
            x2 = x1 + ancho_tecla - 2
            y2 = y1 + alto_tecla
            
            # Crear rectángulo blanco
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black", width=2)
            texto = self.canvas.create_text(x1 + ancho_tecla//2, y2 - 15, text=nota, font=("Arial", 12, "bold"))
            
            # Eventos
            self.canvas.tag_bind(rect, "<Button-1>", lambda e, n=nota: self.tocar_nota(n))
            self.canvas.tag_bind(texto, "<Button-1>", lambda e, n=nota: self.tocar_nota(n))

        # Teclas negras (sostenidos)
        sostenidos = ["C#", "D#", "F#", "G#", "A#"]
        posiciones = [0.7, 1.7, 3.7, 4.7, 5.7]  # Entre las teclas blancas
        ancho_negra = 50
        alto_negra = 80
        
        for i, nota in enumerate(sostenidos):
            x1 = 50 + posiciones[i] * ancho_tecla - ancho_negra//2
            y1 = 30
            x2 = x1 + ancho_negra
            y2 = y1 + alto_negra
            
            # Crear rectángulo negro
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="gray", width=1)
            texto = self.canvas.create_text(x1 + ancho_negra//2, y2 - 15, text=nota, font=("Arial", 10, "bold"), fill="white")
            
            # Eventos
            self.canvas.tag_bind(rect, "<Button-1>", lambda e, n=nota: self.tocar_nota(n))
            self.canvas.tag_bind(texto, "<Button-1>", lambda e, n=nota: self.tocar_nota(n))

    def tocar_nota(self, nota):
        self.historial.append(NotaTocada(nota, "Nota"))
        self.actualizar_historial()

    def deshacer_nota(self):
        if self.historial:
            self.historial.pop()
            self.actualizar_historial()
        else:
            messagebox.showinfo("Atención", "El historial está vacío.")

    def ver_ultima(self):
        if self.historial:
            ultima = self.historial[-1]
            messagebox.showinfo("Último Elemento", str(ultima))
        else:
            messagebox.showinfo("Atención", "No hay elementos en el historial.")

    def limpiar_historial(self):
        self.historial.clear()
        self.actualizar_historial()

    def actualizar_historial(self):
        self.texto_historial.config(state="normal")
        self.texto_historial.delete("1.0", tk.END)
        for nota in reversed(self.historial):
            self.texto_historial.insert(tk.END, str(nota) + "\n")
        self.texto_historial.config(state="disabled")

HistorialNotasGUI()