import sqlite3

databaseName = 'ticketsystem.db'
conn = sqlite3.connect(databaseName)
print("Opened database successfully")

issueNumber = 0
cur = conn.cursor()


def initialize_issue_number():
    global issueNumber
    issueNumber = 1


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


def is_employee(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                    WHERE EmployeeID=?''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


def is_admin(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                WHERE EmployeeID=?
                AND Admin=1''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


def is_tech(employeeID):
    ID = str(employeeID)
    cur.execute('''SELECT * FROM Employees
                WHERE EmployeeID=?
                AND Tech=1''', (ID,))
    if cur.fetchone():
        return True
    else:
        return False


def insert_into_employees(employeeID, employeeName, admin, tech):
    sql = '''INSERT INTO Employees (EmployeeID, EmployeeName, Admin, Tech)
                    Values (?, ?, ?, ?)'''
    package = (employeeID, employeeName, admin, tech)
    cur.execute(sql, package)
    conn.commit()
    if admin:
        print("Inserted Admin into employee table")
    if tech:
        print("Inserted Tech into employee table")
    if not tech and not admin:
        print("Inserted Employee into employee table")


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


def close_database():
    conn.close()
