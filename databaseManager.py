import sqlite3

databaseName = 'ticketsystem.db'
conn = sqlite3.connect(databaseName)
print("Opened database successfully")

issueNumber = 0
cur = conn.cursor()


# This initializes the issue number that keeps track of the number of issues
def initialize_issue_number():
    global issueNumber
    issueNumber = 1


# This creates the Employees and Issues Table
def create_tables():
    conn.execute(
        '''CREATE TABLE Employees (
        EmployeeID       INTEGER(6) PRIMARY KEY
                                 UNIQUE
                                 NOT NULL,
        EmployeeName     STRING  NOT NULL,
        Admin            BOOLEAN NOT NULL,
        Tech             BOOLEAN NOT NULL
    );''')
    print("Table Employee created successfully")

    conn.execute(
        '''CREATE TABLE Issues (
    Name            STRING  NOT NULL,
    Subject         STRING  NOT NULL,
    Description     STRING  NOT NULL,
    [Urgency Level] INTEGER,
    AssignedTech    STRING,
    AssignedTechID  INTEGER,
    IssueID         INTEGER PRIMARY KEY
                            NOT NULL
                            UNIQUE
);
'''
    )
    print("Table Issues created successfully")


# This function returns all employees and their info as a list of tuples
def return_employees():
    data = cur.execute('''Select * FROM Employees''')

    listData = []
    for row in data:
        print(row)
        listData.append(row)

    print(listData)
    print(len(listData))
    return listData


# This function checks to see if the given ID is an Employee
def is_employee(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                    WHERE EmployeeID=?''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


# This function checks to see if the given ID is an Admin
def is_admin(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                WHERE EmployeeID=?
                AND Admin=1''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


# This function checks to see if the given ID is a Tech
def is_tech(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                WHERE EmployeeID=?
                AND Tech=1''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


# This function allows the insertion of employees into the employees table.
def insert_into_employees(employeeID, employeeName, admin, tech):
    print("Inserting new employee...\n")
    sql = '''INSERT INTO Employees (EmployeeID, EmployeeName, Admin, Tech)
                    Values (?, ?, ?, ?)'''
    package = (employeeID, employeeName, admin, tech)
    cur.execute(sql, package)
    conn.commit()
    if admin == 1:
        print("Inserted Admin into employee table")
    if tech == 1:
        print("Inserted Tech into employee table")
    if not tech and not admin:
        print("Inserted Employee into employee table")


# This functions allows the insertion of issues into the issues table.
def insert_into_issues(name, subject, description):
    global issueNumber
    sql = '''INSERT INTO Issues (Name, Subject, Description, IssueID)
                 VALUES (?, ?, ?, ?) '''
    package = (name, subject, description, issueNumber)
    issueNumber += 1
    print(issueNumber)
    cur.execute(sql, package)
    conn.commit()
    print("Inserted issue into issue table.")


# This function closes the database.
def close_database():
    conn.close()
