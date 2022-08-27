from email import message_from_binary_file
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.calc import calc


class App:
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        self.usuario.delete("0", "end")
        self.password.delete("0", "end")
        if (usu == 'root' and password == 'klarotyc'):
            self.ventana.destroy()
            calc()
        else:
            messagebox.showerror(
                message='Usuario o contraseña incorrectos', title='Error al Iniciar Sesion')

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Iniciar Sesion")
        self.ventana.iconbitmap('./images/calc.ico')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen('./images/calculadora.png', (200, 200))

        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300,
                              relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame form title
        frame_form_top = tk.Frame(
            frame_form, height=50, relief=tk.SOLID, bd=0, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(
            frame_form_top, text="Iniciar Sesion", font=('Times', 30), fg="#666a88", pady=50, bg="#fcfcfc")
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame form fill
        frame_form_fill = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(
            frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(
            frame_form_fill, text="Iniciar Sesion", font=('Times', 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()
