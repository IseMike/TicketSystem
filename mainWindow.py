from employeeView import *
import os.path

file_path = 'ticketsystem.db'


def open_new_window(num):
    mainWindow.destroy()
    if num == 1:
        open_employee_view()


if __name__ == '__main__':
    if not os.path.isfile(file_path):
        print("Database does not exist yet")
        from databaseManager import *
        create_tables()
        initialize_issue_number()
    if os.stat(file_path).st_size == 0:
        print("Database does not contain any tables")
        from databaseManager import *
        initialize_issue_number()
        create_tables()
    else:
        print("Database exists and has tables in it")
        from databaseManager import *
    mainWindow = tk.Tk()
    mainWindow.title(" Ticket System Application ")
    mainWindow.geometry("600x400")

    canvas = tk.Canvas(mainWindow, width=400, height=300)
    canvas.pack()

    storeLabel = tk.Label(mainWindow, text='Store ID: ')
    canvas.create_window(162, 75, window=storeLabel)
    storeEntry = tk.Entry(mainWindow)
    canvas.create_window(250, 75, window=storeEntry)

    employeeLabel = tk.Label(mainWindow, text='Employee ID: ')
    canvas.create_window(150, 100, window=employeeLabel)
    nameEntry = tk.Entry(mainWindow)
    canvas.create_window(250, 100, window=nameEntry)

    button1 = tk.Button(mainWindow, text='Continue', command=lambda: open_new_window(1))
    canvas.create_window(200, 300, window=button1)

    mainWindow.mainloop()
