from tkinter import *


class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.config(bg="white")
        self.root.geometry(f"1280x720+100+50")
        self.root.resizable(False, False)
        title = Label(
            self.root,
            text="Employee Payroll Management System",
            font=("times new roman", 30, "bold"),
            bg="#262626", fg="white",
            anchor="w", padx=10
        )
        title.place(x=0, y=0, relwidth=1)

        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white" )
        Frame1.place(x= 10, y=70, width=750, height=630)

        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=500, height=300)

        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=380, width=500, height=320)


win = Tk()
employeeSystem = EmployeeSystem(win)
win.mainloop()