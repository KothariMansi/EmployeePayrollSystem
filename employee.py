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
            anchor="w", padx=350
        )
        title.place(x=0, y=0, relwidth=1)

        #===========Frame 1 ==============
        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white" )
        Frame1.place(x= 10, y=70, width=750, height=630)

        title = Label(
            Frame1,text="Employee Details",font=("times new roman", 20, "bold"),
            bg="lightgray", fg="black",anchor="w", padx=10
        )
        title.place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(Frame1, text="Employee Code", font=("times new roman", 15, "normal"), bg="white")
        lbl_emp_code.place(x=10, y=70)
        txt_emp_code = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_emp_code.place(x=150, y=70, width=200)

        #---------
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 15, "normal"), bg="white")
        lbl_designation.place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_designation.place(x=150, y=120, width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 15, "normal"), bg="white")
        lbl_doj.place(x=370, y=120)
        txt_doj = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_doj.place(x=510, y=120, width=200)

        # ---------
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 15, "normal"), bg="white")
        lbl_name.place(x=10, y=170)
        txt_name = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_name.place(x=150, y=170, width=200)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 15, "normal"), bg="white")
        lbl_dob.place(x=370, y=170)
        txt_dob = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_dob.place(x=510, y=170, width=200)

        # ---------
        lbl_age = Label(Frame1, text="Age", font=("times new roman", 15, "normal"), bg="white")
        lbl_age.place(x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_age.place(x=150, y=220, width=200)

        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 15, "normal"), bg="white")
        lbl_experience.place(x=370, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_experience.place(x=510, y=220, width=200)

        # ---------
        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 15, "normal"), bg="white")
        lbl_gender.place(x=10, y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_gender.place(x=150, y=270, width=200)

        lbl_proof_id = Label(Frame1, text="Proof ID", font=("times new roman", 15, "normal"), bg="white")
        lbl_proof_id.place(x=370, y=270)
        txt_proof_id = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_proof_id.place(x=510, y=270, width=200)

        # ---------
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 15, "normal"), bg="white")
        lbl_email.place(x=10, y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_email.place(x=150, y=320, width=200)

        lbl_contact = Label(Frame1, text="Contact No", font=("times new roman", 15, "normal"), bg="white")
        lbl_contact.place(x=370, y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_contact.place(x=510, y=320, width=200)

        # ---------
        lbl_hired = Label(Frame1, text="Hired Location", font=("times new roman", 15, "normal"), bg="white")
        lbl_hired.place(x=10, y=370)
        txt_hired = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_hired.place(x=150, y=370, width=200)

        lbl_contact = Label(Frame1, text="Status", font=("times new roman", 15, "normal"), bg="white")
        lbl_contact.place(x=370, y=370)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_contact.place(x=510, y=370, width=200)

        # ---------
        lbl_address = Label(Frame1, text="Address", font=("times new roman", 15, "normal"), bg="white")
        lbl_address.place(x=10, y=420)
        txt_address = Text(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_address.place(x=150, y=420, width=560, height=150)

        # ===========Frame 2 ==============
        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=500, height=300)

        # ===========Frame 3 ==============
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=380, width=500, height=320)


win = Tk()
employeeSystem = EmployeeSystem(win)
win.mainloop()