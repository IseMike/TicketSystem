import tkinter as tk
from databaseManager import *

left_padding = 0
right_padding = 0


# This is a helper function for the other open functions
def open_helper(admin, issue, employee, window):
    if admin:
        window.destroy()
        open_admin_view()
    if issue:
        window.destroy()
        open_issues_table()
    if employee:
        window.destroy()
        open_employee_table()


def insert_and_open(employeeID, name, admin, tech, window):
    insert_into_employees(employeeID, name, admin, tech)
    open_helper(False, False, True, window)


# This opens the employee table view.
# This contains a table of all employees and a way to delete/add employees.
def open_employee_table():
    employeeWindow = tk.Tk()
    employeeWindow.title(" Employee Table ")
    employeeWindow.geometry("600x400")

    bottom_frame = tk.Frame(employeeWindow)

    bottom_frame.grid(row=1, column=0)  # remove columnspan or set it to 1
    spacer1 = tk.Label(bottom_frame, text="")
    spacer1.grid(column=2)

    IDText = tk.Label(bottom_frame, text="ID")
    IDText.grid(row=2, column=1)
    nameText = tk.Label(bottom_frame, text="Name")
    nameText.grid(row=2, column=2)
    adminText = tk.Label(bottom_frame, text="Admin?")
    adminText.grid(row=2, column=3)
    techText = tk.Label(bottom_frame, text="Tech?")
    techText.grid(row=2, column=4)

    table = return_employees()
    for i in range(len(table)):
        for j in range(4):
            label1 = tk.Entry(bottom_frame, width=20)
            label1.grid(row=i + 3, column=j + 1)
            label1.insert(tk.END, table[i][j])

    label2 = tk.Label(bottom_frame, text='ID:')
    label2.grid(row=15, column=1)
    idEntry = tk.Entry(bottom_frame)
    idEntry.grid(row=16, column=1)

    label3 = tk.Label(bottom_frame, text='Name:')
    label3.grid(row=15, column=2)
    nameEntry = tk.Entry(bottom_frame)
    nameEntry.grid(row=16, column=2)

    label4 = tk.Label(bottom_frame, text='Admin?:')
    label4.grid(row=15, column=3)
    adminEntry = tk.Entry(bottom_frame)
    adminEntry.grid(row=16, column=3)

    label5 = tk.Label(bottom_frame, text='Tech?:')
    label5.grid(row=15, column=4)
    techEntry = tk.Entry(bottom_frame)
    techEntry.grid(row=16, column=4)

    button1 = tk.Button(bottom_frame, text='Back', command=lambda: open_helper(True, False, False, employeeWindow))
    button1.grid(row=25, column=2)

    button2 = tk.Button(bottom_frame, text='Create New Employee', command=lambda: insert_and_open(
        idEntry.get(), nameEntry.get(), adminEntry.get(), techEntry.get(), employeeWindow
    ))

    button2.grid(row=20, column=4)
    employeeWindow.mainloop()


# This opens the issue table view.
# This contains a table of all issues and will allow an admin to set the severity
# of the issue and assign a tech to each issue.
def open_issues_table():
    issuesWindow = tk.Tk()
    issuesWindow.title(" Issues Table ")
    issuesWindow.geometry("600x400")

    canvas = tk.Canvas(issuesWindow, width=400, height=300)
    canvas.pack()

    button1 = tk.Button(issuesWindow, text='Back', command=lambda: open_helper(True, False, False, issuesWindow))
    canvas.create_window(200, 300, window=button1)

    issuesWindow.mainloop()


# This opens the admin main menu.
# This contains two buttons to allow the admin to either check the
# Employee table or the Issues table.
def open_admin_view():
    window = tk.Tk()
    window.title(" Ticket System Application ")
    window.geometry("600x400")

    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()

    button1 = tk.Button(window, text='Check Employees', command=lambda: open_helper(False, False, True, window))
    canvas.create_window(170, 300, window=button1)

    button2 = tk.Button(window, text='Check Issues', command=lambda: open_helper(False, True, False, window))
    canvas.create_window(270, 300, window=button2)

    window.mainloop()
