from tkinter import *
import tkinter as tk
from employeeView import *


def open_new_window(num):
    mainWindow.destroy()
    if num == 1:
        open_employee_view()


mainWindow = tk.Tk()
mainWindow.title(" Ticket System Application ")
mainWindow.geometry("600x400")

canvas = tk.Canvas(mainWindow, width=400, height=300)
canvas.pack()

storeLabel = tk.Label(mainWindow, text='Store ID: ')
canvas.create_window(150, 75, window=storeLabel)
storeEntry = tk.Entry(mainWindow)
canvas.create_window(250, 75, window=storeEntry)

employeeLabel = tk.Label(mainWindow, text='Employee ID: ')
canvas.create_window(150, 100, window=employeeLabel)
nameEntry = tk.Entry(mainWindow)
canvas.create_window(250, 100, window=nameEntry)

button1 = tk.Button(mainWindow, text='Continue', command=lambda: open_new_window(1))
canvas.create_window(200, 300, window=button1)

mainWindow.mainloop()
