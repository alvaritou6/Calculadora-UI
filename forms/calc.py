import tkinter as tk
from tkinter.font import BOLD
from turtle import window_height
import util.generic as utl

i = 0


class calc:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.iconbitmap('./images/calc.ico')
        self.ventana.resizable(width=0, height=0)

        # Entrada
        e_texto = tk.Entry(self.ventana, font=('Calibri', 20))
        e_texto.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

        # Funciones
        def click_boton(valor):
            global i
            e_texto.insert(i, valor)
            i += 1

        def borrar():
            e_texto.delete(0, "end")
            i = 0

        def resolver():
            ecuacion = e_texto.get()
            resultado = eval(ecuacion)
            e_texto.delete(0, "end")
            e_texto.insert(0, resultado)
            i = 0

        # Botones
        boton1 = tk.Button(self.ventana, text="1", width=5,
                           height=2, command=lambda: click_boton(1))
        boton2 = tk.Button(self.ventana, text="2", width=5,
                           height=2, command=lambda: click_boton(2))
        boton3 = tk.Button(self.ventana, text="3", width=5,
                           height=2, command=lambda: click_boton(3))
        boton4 = tk.Button(self.ventana, text="4", width=5,
                           height=2, command=lambda: click_boton(4))
        boton5 = tk.Button(self.ventana, text="5", width=5,
                           height=2, command=lambda: click_boton(5))
        boton6 = tk.Button(self.ventana, text="6", width=5,
                           height=2, command=lambda: click_boton(6))
        boton7 = tk.Button(self.ventana, text="7", width=5,
                           height=2, command=lambda: click_boton(7))
        boton8 = tk.Button(self.ventana, text="8", width=5,
                           height=2, command=lambda: click_boton(8))
        boton9 = tk.Button(self.ventana, text="9", width=5,
                           height=2, command=lambda: click_boton(9))
        boton0 = tk.Button(self.ventana, text="0", width=13,
                           height=2, command=lambda: click_boton(0))

        boton_borrar = tk.Button(
            self.ventana, text="AC", width=5, height=2, command=lambda: borrar())
        boton_parentesis1 = tk.Button(
            self.ventana, text="(", width=5, height=2, command=lambda: click_boton("("))
        boton_parentesis2 = tk.Button(
            self.ventana, text=")", width=5, height=2, command=lambda: click_boton(")"))
        boton_punto = tk.Button(
            self.ventana, text=".", width=5, height=2, command=lambda: click_boton("."))
        boton_igual = tk.Button(self.ventana, text="=",
                                width=5, height=2, command=lambda: resolver())

        boton_sum = tk.Button(self.ventana, text="+", width=5,
                              height=2, command=lambda: click_boton("+"))
        boton_resta = tk.Button(
            self.ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
        boton_div = tk.Button(self.ventana, text="÷", width=5,
                              height=2, command=lambda: click_boton("/"))
        boton_mult = tk.Button(
            self.ventana, text="x", width=5, height=2, command=lambda: click_boton("*"))

        # Posicionando Botones
        boton_borrar.grid(row=1, column=0, padx=5, pady=5)
        boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
        boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
        boton_div.grid(row=1, column=3, padx=5, pady=5)

        boton7.grid(row=2, column=0, padx=5, pady=5)
        boton8.grid(row=2, column=1, padx=5, pady=5)
        boton9.grid(row=2, column=2, padx=5, pady=5)
        boton_mult.grid(row=2, column=3, padx=5, pady=5)

        boton4.grid(row=3, column=0, padx=5, pady=5)
        boton5.grid(row=3, column=1, padx=5, pady=5)
        boton6.grid(row=3, column=2, padx=5, pady=5)
        boton_sum.grid(row=3, column=3, padx=5, pady=5)

        boton1.grid(row=4, column=0, padx=5, pady=5)
        boton2.grid(row=4, column=1, padx=5, pady=5)
        boton3.grid(row=4, column=2, padx=5, pady=5)
        boton_resta.grid(row=4, column=3, padx=5, pady=5)

        boton0.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
        boton_punto.grid(row=5, column=2, padx=5, pady=5)
        boton_igual.grid(row=5, column=3, padx=5, pady=5)

        self.ventana.mainloop()
