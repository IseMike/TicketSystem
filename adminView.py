import tkinter as tk
from databaseManager import *

left_padding = 0
right_padding = 0
tech = "Select a tech"


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


# Helper function for buttons who need to insert new information into the database
# and open a new window
def insert_and_open(employeeID, name, admin, tech, window):
    insert_into_employees(employeeID, name, admin, tech)
    open_helper(False, False, True, window)


# Helper function for buttons who need to delete an employee
# and open a new window
def delete_emp_and_open(employeeID, window):
    delete_employee(employeeID)
    open_helper(False, False, True, window)


# Helper function for buttons who need to delete an issue
# and open a new window
def delete_iss_and_open(issueID, window):
    delete_issue(issueID)
    open_helper(False, True, False, window)


# This opens the employee table view.
# This contains a table of all employees and a way to delete/add employees.
def open_employee_table():
    employeeWindow = tk.Tk()
    employeeWindow.title(" Employee Table ")
    employeeWindow.geometry("600x400")

    bottom_frame = tk.Frame(employeeWindow)

    bottom_frame.grid(row=1, column=0)
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
            label1.configure(state='disabled')
        button2 = tk.Button(bottom_frame, text='Delete', command=lambda x=i: delete_emp_and_open(table[x][0],
                                                                                                 employeeWindow))
        button2.grid(row=i + 3, column=j + 2)

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
    issuesWindow.geometry("1200x800")

    listOfTechs = return_techs()
    techNames = []
    print(listOfTechs[0][1])
    for i in listOfTechs:
        techNames.append(i[1])

    bottom_frame = tk.Frame(issuesWindow)

    bottom_frame.grid(row=1, column=0)
    spacer1 = tk.Label(bottom_frame, text="")
    spacer1.grid(column=2)

    nameText = tk.Label(bottom_frame, text="Name")
    nameText.grid(row=2, column=1)
    subjectText = tk.Label(bottom_frame, text="Subject")
    subjectText.grid(row=2, column=2)
    descText = tk.Label(bottom_frame, text="Description")
    descText.grid(row=2, column=3)
    urgText = tk.Label(bottom_frame, text="Urgency Level")
    urgText.grid(row=2, column=4)
    techText = tk.Label(bottom_frame, text="Assigned Tech")
    techText.grid(row=2, column=5)
    issueIDText = tk.Label(bottom_frame, text="Issue ID")
    issueIDText.grid(row=2, column=6)

    table = return_issues_admin()
    for i in range(len(table)):
        print(table[i][0])
        for j in range(6):
            if j != 4:
                if j == 2:
                    label1 = tk.Text(bottom_frame, width=30, height=3)
                else:
                    label1 = tk.Entry(bottom_frame, width=20)
                label1.grid(row=i + 3, column=j + 1)
                label1.insert(tk.END, table[i][j])
                if j != 3:
                    urgencyLabel = label1
                    label1.configure(state='disabled')
            else:
                optionChosen = tk.StringVar(bottom_frame)
                optionChosen.set("Select a tech")
                combobox1 = tk.OptionMenu(bottom_frame, optionChosen, techNames, command=callback)
                combobox1.grid(row=i + 3, column=5)
        button2 = tk.Button(bottom_frame, text='Delete', command=lambda x=i: delete_iss_and_open(table[x][5],
                                                                                                 issuesWindow))
        button2.grid(row=i + 3, column=j + 2)
        button3 = tk.Button(bottom_frame, text='Update', command=lambda x=i: update_issues(table[x][0], table[x][1],
                                                                                           table[x][2],
                                                                                           urgencyLabel.get(), tech[0],
                                                                                           table[x][5]))
        button3.grid(row=i + 3, column=j + 3)

    button1 = tk.Button(issuesWindow, text='Back', command=lambda: open_helper(True, False, False, issuesWindow))
    button1.grid(row=25, column=2)

    issuesWindow.mainloop()


def callback(selection):
    global tech
    print(selection)
    tech = selection


# This opens the admin main menu.
# This contains two buttons to allow the admin to either check the
# Employee table or the Issues table.
def open_admin_view():
    window = tk.Tk()
    window.title(" Ticket System Application ")
    window.geometry("600x400")

    canvas = tk.Canvas(window, width=400, height=300)
    canvas.pack()

    button1 = tk.Button(window, text='Check Employees', width=20, height=5,
                        command=lambda: open_helper(False, False, True, window))
    canvas.create_window(220, 100, window=button1)

    button2 = tk.Button(window, text='Check Issues', width=20, height=5,
                        command=lambda: open_helper(False, True, False, window))
    canvas.create_window(220, 250, window=button2)

    window.mainloop()
