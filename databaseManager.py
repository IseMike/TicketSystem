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
    UrgencyLevel    INTEGER,
    AssignedTech    STRING,
    IssueID         INTEGER PRIMARY KEY
                            NOT NULL
                            UNIQUE
    );''')
    print("Table Issues created successfully")

    conn.execute(
        '''CREATE TABLE CompletedIssues (
    Name            STRING  NOT NULL,
    Subject         STRING  NOT NULL,
    Description     STRING  NOT NULL,
    UrgencyLevel    INTEGER,
    AssignedTech    STRING,
    IssueID         INTEGER PRIMARY KEY
                            NOT NULL
                            UNIQUE
    );''')
    print("Table CompletedIssues created successfully")


# This function updates the Issues table
def update_issues(name, subject, description, urgencyLevel, assignedTech, issueID):
    print(type(assignedTech))
    print(name + " " + subject + " " + description + " " + str(urgencyLevel) + " " + assignedTech + " " + str(issueID))
    cur.execute('''UPDATE Issues
                    SET Name=?, Subject=?, Description=?, UrgencyLevel=?,
                    AssignedTech=?, IssueID=?
                    WHERE issueID=?''',
                (name, subject, description, urgencyLevel,
                 assignedTech, issueID,
                 issueID))
    conn.commit()


# This function deletes an employee using an employee ID
def delete_employee(employeeID):
    ID = str(employeeID)
    cur.execute('''DELETE FROM Employees
                    WHERE EmployeeID=?''', (ID,))
    print('Deleting Employee: ' + ID)
    conn.commit()


# This function deletes an issue using an issue ID
def delete_issue(issueID):
    ID = str(issueID)
    cur.execute('''DELETE FROM Issues
                    WHERE IssueID=?''', (ID,))
    print('Deleting Issue #' + ID)
    conn.commit()


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


# This function returns all techs.
def return_techs():
    data = cur.execute('''Select EmployeeID, EmployeeName
                            FROM Employees
                            WHERE Tech=1''')
    listData = []
    for row in data:
        listData.append(row)

    return listData


# This function returns all issues and their info as a list of tuples
def return_issues_admin():
    data = cur.execute('''Select * FROM Issues''')

    listData = []
    for row in data:
        print(row)
        listData.append(row)

    return listData


# This function returns all completed issues and their info as a list of tuples
def return_completed_admin():
    data = cur.execute('''Select * FROM CompletedIssues''')
    listData = []
    for row in data:
        print(row)
        listData.append(row)
    return listData


# This function given an employees ID returns the employees name
def return_employee_name(employeeID):
    print('This is the employeeID: ' + employeeID)
    cur.execute('''Select EmployeeName FROM Employees
                    WHERE EmployeeID=?''', (employeeID,))
    return cur.fetchone()


# This function returns all issues that have an urgency level assigned by
# an admin and are assigned to a specified tech
def return_issues_tech(techID):
    techName = return_employee_name(techID)
    data = cur.execute('''Select Name, Subject, Description, UrgencyLevel, IssueID 
                            FROM Issues
                            WHERE UrgencyLevel!=0
                            AND AssignedTech=?''', techName)
    listData = []
    for row in data:
        listData.append(row)

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
    cur.execute('''SELECT max(IssueID)
                    FROM Issues''')
    row = cur.fetchone()
    print(row)
    if row[0] is None:
        print('row is None')
        issueNumber = 1
    else:
        issueNumber = row[0] + 1
    sql = '''INSERT INTO Issues (Name, Subject, Description, UrgencyLevel, AssignedTech, IssueID)
                                VALUES (?, ?, ?, ?, ?, ?) '''
    package = (name, subject, description, 0, "", issueNumber)
    print(issueNumber)
    cur.execute(sql, package)
    conn.commit()
    print("Inserted issue into issue table.")


# This function allows the insertion of issues into the completed issues table
def insert_into_completed(name, subject, description, urgencyLevel, assignedTech, issueID):
    package = (name, subject, description, urgencyLevel, assignedTech, issueID)
    print(package)
    cur.execute('''INSERT INTO CompletedIssues (Name, Subject, Description, UrgencyLevel, AssignedTech, IssueID)
                                                VALUES(?, ?, ?, ?, ?, ?)''', (name, subject, description,
                                                                              urgencyLevel, assignedTech, issueID))
    conn.commit()
    print("Insert issue into completed issue table")


# This function closes the database.
def close_database():
    conn.close()
