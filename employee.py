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
        Frame1.place(x= 10, y=70, width=730, height=630)

        title2 = Label(
            Frame1,text="Employee Details",font=("times new roman", 20, "bold"),
            bg="lightgray", fg="black",anchor="w", padx=10
        )
        title2.place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(Frame1, text="Employee Code", font=("times new roman", 15, "normal"), bg="white")
        lbl_emp_code.place(x=10, y=70)
        txt_emp_code = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_emp_code.place(x=150, y=70, width=200)

        btn_search = Button(Frame1, text="Search", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_search.place(x=370, y=68, width=100, height=30)

        # ---------Row1
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 15, "normal"), bg="white")
        lbl_designation.place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_designation.place(x=150, y=120, width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 15, "normal"), bg="white")
        lbl_doj.place(x=370, y=120)
        txt_doj = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_doj.place(x=510, y=120, width=200)

        # ---------Row2
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 15, "normal"), bg="white")
        lbl_name.place(x=10, y=170)
        txt_name = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_name.place(x=150, y=170, width=200)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 15, "normal"), bg="white")
        lbl_dob.place(x=370, y=170)
        txt_dob = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_dob.place(x=510, y=170, width=200)

        # ---------Row3
        lbl_age = Label(Frame1, text="Age", font=("times new roman", 15, "normal"), bg="white")
        lbl_age.place(x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_age.place(x=150, y=220, width=200)

        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 15, "normal"), bg="white")
        lbl_experience.place(x=370, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_experience.place(x=510, y=220, width=200)

        # ---------Row4
        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 15, "normal"), bg="white")
        lbl_gender.place(x=10, y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_gender.place(x=150, y=270, width=200)

        lbl_proof_id = Label(Frame1, text="Proof ID", font=("times new roman", 15, "normal"), bg="white")
        lbl_proof_id.place(x=370, y=270)
        txt_proof_id = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_proof_id.place(x=510, y=270, width=200)

        # ---------Row5
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 15, "normal"), bg="white")
        lbl_email.place(x=10, y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_email.place(x=150, y=320, width=200)

        lbl_contact = Label(Frame1, text="Contact No", font=("times new roman", 15, "normal"), bg="white")
        lbl_contact.place(x=370, y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_contact.place(x=510, y=320, width=200)

        # ---------Row6
        lbl_hired = Label(Frame1, text="Hired Location", font=("times new roman", 15, "normal"), bg="white")
        lbl_hired.place(x=10, y=370)
        txt_hired = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_hired.place(x=150, y=370, width=200)

        lbl_contact = Label(Frame1, text="Status", font=("times new roman", 15, "normal"), bg="white")
        lbl_contact.place(x=370, y=370)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_contact.place(x=510, y=370, width=200)

        # ---------Row7
        lbl_address = Label(Frame1, text="Address", font=("times new roman", 15, "normal"), bg="white")
        lbl_address.place(x=10, y=420)
        txt_address = Text(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        txt_address.place(x=150, y=420, width=560, height=150)

        # ===========Frame 2 ==============
        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=750, y=70, width=520, height=310)

        title3 = Label(
            Frame2, text="Employee Salary", font=("times new roman", 20, "bold"),
            bg="lightgray", fg="black", anchor="w", padx=10
        )
        title3.place(x=0, y=0, relwidth=1)

        # ---------Row1
        lbl_month = Label(Frame2, text="Month", font=("times new roman", 14, "normal"), bg="white")
        lbl_month.place(x=10, y=70)
        txt_month = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_month.place(x=65, y=70, width=100)

        lbl_doj = Label(Frame2, text="Year", font=("times new roman", 14, "normal"), bg="white")
        lbl_doj.place(x=165, y=70)
        txt_doj = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_doj.place(x=207, y=70, width=100)

        lbl_doj = Label(Frame2, text="Basic Salary", font=("times new roman", 14, "normal"), bg="white")
        lbl_doj.place(x=305, y=70)
        txt_doj = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_doj.place(x=405, y=70, width=100)

        # ---------Row2
        lbl_total_days = Label(Frame2, text="Total Days", font=("times new roman", 14, "normal"), bg="white")
        lbl_total_days.place(x=10, y=120)
        txt_total_days = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_total_days.place(x=100, y=120, width=150)

        lbl_absent = Label(Frame2, text="Absents", font=("times new roman", 14, "normal"), bg="white")
        lbl_absent.place(x=270, y=120)
        txt_absent = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_absent.place(x=340, y=120, width=150)

        # ---------Row3
        lbl_medical = Label(Frame2, text="Medical", font=("times new roman", 14, "normal"), bg="white")
        lbl_medical.place(x=10, y=170)
        txt_medical = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_medical.place(x=100, y=170, width=100)

        lbl_provident_fund = Label(Frame2, text="Provident Fund", font=("times new roman", 14, "normal"), bg="white")
        lbl_provident_fund.place(x=215, y=170)
        txt_provident_fund = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_provident_fund.place(x=340, y=170, width=150)

        # ---------Row4
        lbl_convince = Label(Frame2, text="Convince", font=("times new roman", 14, "normal"), bg="white")
        lbl_convince.place(x=10, y=220)
        txt_convince = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_convince.place(x=100, y=220, width=100)

        lbl_net_salary = Label(Frame2, text="Net Salary", font=("times new roman", 14, "normal"), bg="white")
        lbl_net_salary.place(x=215, y=220)
        txt_net_salary = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black")
        txt_net_salary.place(x=340, y=220, width=150)

        # ----------Buttons
        btn_calculate = Button(Frame2, text="Calculate", font=("times new roman", 15, "normal"), bg="#bfc418", fg="black")
        btn_calculate.place(x=170, y=265, width=100, height=30)
        btn_save = Button(Frame2, text="Save", font=("times new roman", 15, "normal"), bg="#32a852", fg="white")
        btn_save.place(x=280, y=265, width=100, height=30)
        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_clear.place(x=390, y=265, width=100, height=30)

        # ===========Frame 3 ==============
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=750, y=390, width=520, height=310)

        # ----------Calculater Frame-------------
        cal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        cal_Frame.place(x=5, y=5, width=270, height=290)

        txt_result = Entry(cal_Frame, font=("times new roman", 20, "normal"), bg="lightgray", fg="black")
        txt_result.place(x=4, y=5, width=260, height=50)

        # ----------Row1---------
        btn_7 = Button(cal_Frame, text="7", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_7.place(x=5, y=62, width=60, height=50)

        btn_8 = Button(cal_Frame, text="8", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_8.place(x=70, y=62, width=60, height=50)

        btn_9 = Button(cal_Frame, text="9", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_9.place(x=135, y=62, width=60, height=50)

        btn_divide = Button(cal_Frame, text="/", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_divide.place(x=200, y=62, width=60, height=50)

        # ----------Row2---------
        btn_4 = Button(cal_Frame, text="4", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_4.place(x=5, y=116, width=60, height=50)

        btn_5 = Button(cal_Frame, text="5", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_5.place(x=70, y=116, width=60, height=50)

        btn_6 = Button(cal_Frame, text="6", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_6.place(x=135, y=116, width=60, height=50)

        btn_multiply = Button(cal_Frame, text="*", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_multiply.place(x=200, y=116, width=60, height=50)

        # ----------Row1---------
        btn_1 = Button(cal_Frame, text="1", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_1.place(x=5, y=170, width=60, height=50)

        btn_2 = Button(cal_Frame, text="2", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_2.place(x=70, y=170, width=60, height=50)

        btn_3 = Button(cal_Frame, text="3", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_3.place(x=135, y=170, width=60, height=50)

        btn_add = Button(cal_Frame, text="-", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_add.place(x=200, y=170, width=60, height=50)

        # ----------Row1---------
        btn_1 = Button(cal_Frame, text="0", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_1.place(x=5, y=225, width=60, height=50)

        btn_2 = Button(cal_Frame, text=".", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_2.place(x=70, y=225, width=60, height=50)

        btn_3 = Button(cal_Frame, text="+", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_3.place(x=135, y=225, width=60, height=50)

        btn_4 = Button(cal_Frame, text="=", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_4.place(x=200, y=225, width=60, height=50)

        # ----------Salary Receipt Frame-------------
        salary_receipt_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        salary_receipt_Frame.place(x=280, y=5, width=225, height=290)

        lbl_salary_receipt = Label(salary_receipt_Frame, text="Salary Receipt", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_salary_receipt.place(x=20, y=10)

        # --------- Frame
        salary_receipt_detail_frame = Frame(salary_receipt_Frame, bg="white", bd=2, relief=RIDGE)
        salary_receipt_detail_frame.place(x=5, y=50, width=210, height=185)

        # ---------Row1
        btn_print = Button(salary_receipt_Frame, text="Print", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_print.place(x=115, y=245, width=100, height=30)

win = Tk()
employeeSystem = EmployeeSystem(win)
win.mainloop()