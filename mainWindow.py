from employeeView import *
from adminView import *
from techView import *
import os.path

file_path = 'ticketsystem.db'


# This function opens a new window depending on whether the employee is
# an Admin, a Tech or a normal employee.
# It will pop up an error message if the ID is not in the employee table.
def open_new_window(ID):
    print(ID)
    admin = False
    tech = False
    employee = False
    if is_admin(ID):
        admin = True
        mainWindow.destroy()
        print("This is an Admin")
        open_admin_view()
    if is_tech(ID):
        tech = True
        mainWindow.destroy()
        print("This is a Tech")
        open_tech_view(ID)
    if is_employee(ID) and not tech and not admin:
        employee = True
        mainWindow.destroy()
        print("This is an employee.")
        open_employee_view()
    if not employee and not tech and not admin:
        print("This is not an employee.")
        l1 = tk.Label(mainWindow, text="Sorry, we could not verify your ID Number.\n Please Try Again",
                      fg='#ff0000')
        canvas.create_window(200, 265, window=l1)


# This function populates the employee table for testing.
def test():
    insert_into_employees(123456, "Isaac", True, False)
    insert_into_employees(234567, "Micah", False, True)
    insert_into_employees(345678, "Derek", False, False)
    insert_into_issues("Joe", "Help", "I need help")
    insert_into_issues("Bob", "Fill", "help")
    insert_into_issues("Ise", "pip", "pop")


if __name__ == '__main__':
    if not os.path.isfile(file_path):
        print("Database does not exist yet")
        from databaseManager import *

        create_tables()
        initialize_issue_number()
        test()
    if os.stat(file_path).st_size == 0:
        print("Database does not contain any tables")
        from databaseManager import *

        initialize_issue_number()
        create_tables()
        test()
    else:
        print("Database exists and has tables in it")
        from databaseManager import *
    mainWindow = tk.Tk()
    mainWindow.title(" Ticket System Application ")
    mainWindow.geometry("600x400")

    canvas = tk.Canvas(mainWindow, width=400, height=300)
    canvas.pack()

    employeeLabel = tk.Label(mainWindow, text='Employee ID: ')
    canvas.create_window(145, 75, window=employeeLabel)
    idEntry = tk.Entry(mainWindow)
    canvas.create_window(250, 75, window=idEntry)

    button1 = tk.Button(mainWindow, text='Continue', command=lambda: open_new_window(idEntry.get()))
    canvas.create_window(200, 300, window=button1)

    mainWindow.mainloop()
