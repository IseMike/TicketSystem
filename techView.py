import tkinter as tk

from databaseManager import *


# Helper function for buttons who need to transfer an issue from the issues table
# to the completed issues table and open a new window
def transfer_issue(name, subject, description, urgencyLevel, assignedTech, issueID, window, techID):
    delete_issue(issueID)
    techName = 'Something went wrong'
    for i in assignedTech:
        techName = i
    insert_into_completed(name, subject, description, urgencyLevel, techName, issueID)
    window.destroy()
    open_tech_view(techID)


# This opens the issue table view.
# This contains a table of all issues and will allow an admin to set the severity
# of the issue and assign a tech to each issue.
def open_tech_view(techID):
    issuesWindow = tk.Tk()
    issuesWindow.title(" Issues Table ")
    issuesWindow.geometry("1200x800")

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
    issueIDText = tk.Label(bottom_frame, text="Issue ID")
    issueIDText.grid(row=2, column=5)

    table = return_issues_tech(techID)
    for i in range(len(table)):
        print(table[i][0])
        for j in range(5):
            if j == 2:
                label1 = tk.Text(bottom_frame, width=30, height=3)
            else:
                label1 = tk.Entry(bottom_frame, width=20)
            label1.grid(row=i + 3, column=j + 1)
            label1.insert(tk.END, table[i][j])
            label1.configure(state='disabled')
        button1 = tk.Button(bottom_frame, text='Solved', command=lambda x=i: transfer_issue(table[x][0], table[x][1],
                                                                                            table[x][2], table[x][3],
                                                                                            return_employee_name(techID)
                                                                                            , table[x][4], issuesWindow,
                                                                                            techID))
        button1.grid(row=i + 3, column=j + 2)

    issuesWindow.mainloop()
