# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:08:12 2024

@author: Antonio
"""

import tkinter as tk
import serial

# Configura el puerto serie
port = 'COM3'  # Cambia esto si tu Arduino está en otro puerto
baudrate = 9600
ser = serial.Serial(port, baudrate)

# Función para encender el LED
def encender_led():
    ser.write(b'b')  # Envía el comando para encender el LED
    print("LED Encendido")

# Función para apagar el LED
def apagar_led():
    ser.write(b'a')  # Envía el comando para apagar el LED
    print("LED Apagado")

# Crear la interfaz gráfica usando Tkinter
root = tk.Tk()
root.title("Control LED")

# Botón para encender el LED
btn_encender = tk.Button(root, text="Encender LED", command=encender_led)
btn_encender.pack(pady=10)

# Botón para apagar el LED
btn_apagar = tk.Button(root, text="Apagar LED", command=apagar_led)
btn_apagar.pack(pady=10)

# Evento para cerrar el puerto serie cuando se cierra la ventana
def on_closing():
    if ser.is_open:
        ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()