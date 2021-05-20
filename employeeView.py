import tkinter as tk
from databaseManager import *


# This stores the Issue that the employee writes into the Issue table.
def store_db(name_entry, subject_entry, desc_entry, window, canvas):
    x1 = name_entry.get()
    x2 = subject_entry.get()
    x3 = desc_entry.get("1.0", 'end-1c')
    l1 = tk.Label(window, text="Thank you, " + x1 + ", an administrator will be with you shortly.\n"
                                                    "You may now close the application.")
    print(x1 + "\n" + x2 + "\n" + x3)
    canvas.create_window(200, 265, window=l1)
    insert_into_issues(x1, x2, x3)
    close_database()


# This opens the employee view.
# Here an employee can report any issues to the Admin.
def open_employee_view():
    window = tk.Tk()
    window.title(" Ticket System Application ")
    window.geometry("600x400")

    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()

    label1 = tk.Label(window, text='Please fill out the ticket below:')
    label1.config(font=('helvetica', 14))
    canvas.create_window(200, 25, window=label1)

    label2 = tk.Label(window, text='Name:')
    canvas.create_window(50, 75, window=label2)
    nameEntry = tk.Entry(window)
    canvas.create_window(140, 75, window=nameEntry)

    label3 = tk.Label(window, text='Subject:')
    canvas.create_window(50, 115, window=label3)
    subjectEntry = tk.Entry(window, width=50)
    canvas.create_window(230, 115, window=subjectEntry)

    label4 = tk.Label(window, text='Description:')
    canvas.create_window(38, 155, window=label4)
    descEntry = tk.Text(window, height=5, width=40)
    canvas.create_window(238, 190, window=descEntry)

    button1 = tk.Button(window, text='Send', command=lambda: store_db(nameEntry, subjectEntry,
                                                                      descEntry, window, canvas))
    canvas.create_window(200, 300, window=button1)

    window.mainloop()
