import sqlite3

databaseName = 'ticketsystem.db'
conn = sqlite3.connect(databaseName)
print("Opened database successfully")

issueNumber = 0


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
        EmployeePassword STRING  UNIQUE
                                 NOT NULL,
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


def insert_into_issues(name, subject, description):
    global issueNumber
    sql = '''INSERT INTO Issues (Name,Subject, Description, IssueID)
                 VALUES (?, ?, ?, ?) '''
    cur = conn.cursor()
    package = (name, subject, description, issueNumber)
    issueNumber += 1
    print(issueNumber)
    cur.execute(sql, package)
    conn.commit()
    print("Inserted issue into issues database.")


def close_database():
    conn.close()
