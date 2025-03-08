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

        #------------Variables----------
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_doj = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_age = StringVar()
        self.var_experience =StringVar()
        self.var_gender = StringVar()
        self.var_proof_id = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_hired_location = StringVar()
        self.var_status = StringVar()

        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white" )
        Frame1.place(x= 10, y=70, width=730, height=630)

        title2 = Label(
            Frame1,text="Employee Details",font=("times new roman", 20, "bold"),
            bg="lightgray", fg="black",anchor="w", padx=10
        )
        title2.place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(Frame1, text="Employee Code", font=("times new roman", 15, "normal"), bg="white")
        lbl_emp_code.place(x=10, y=70)
        txt_emp_code = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black",  textvariable=self.var_emp_code)
        txt_emp_code.place(x=150, y=70, width=200)

        btn_search = Button(Frame1, text="Search", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_search.place(x=370, y=68, width=100, height=30)

        # ---------Row1
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 15, "normal"), bg="white")
        lbl_designation.place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_designation)
        txt_designation.place(x=150, y=120, width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 15, "normal"), bg="white")
        lbl_doj.place(x=370, y=120)
        txt_doj = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_doj)
        txt_doj.place(x=510, y=120, width=200)

        # ---------Row2
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 15, "normal"), bg="white")
        lbl_name.place(x=10, y=170)
        txt_name = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_name)
        txt_name.place(x=150, y=170, width=200)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 15, "normal"), bg="white")
        lbl_dob.place(x=370, y=170)
        txt_dob = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_dob)
        txt_dob.place(x=510, y=170, width=200)

        # ---------Row3
        lbl_age = Label(Frame1, text="Age", font=("times new roman", 15, "normal"), bg="white")
        lbl_age.place(x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_age)
        txt_age.place(x=150, y=220, width=200)

        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 15, "normal"), bg="white")
        lbl_experience.place(x=370, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_experience)
        txt_experience.place(x=510, y=220, width=200)

        # ---------Row4
        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 15, "normal"), bg="white")
        lbl_gender.place(x=10, y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_gender)
        txt_gender.place(x=150, y=270, width=200)

        lbl_proof_id = Label(Frame1, text="Proof ID", font=("times new roman", 15, "normal"), bg="white")
        lbl_proof_id.place(x=370, y=270)
        txt_proof_id = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_proof_id)
        txt_proof_id.place(x=510, y=270, width=200)

        # ---------Row5
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 15, "normal"), bg="white")
        lbl_email.place(x=10, y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_email)
        txt_email.place(x=150, y=320, width=200)

        lbl_contact = Label(Frame1, text="Contact No", font=("times new roman", 15, "normal"), bg="white")
        lbl_contact.place(x=370, y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_contact)
        txt_contact.place(x=510, y=320, width=200)

        # ---------Row6
        lbl_hired = Label(Frame1, text="Hired Location", font=("times new roman", 15, "normal"), bg="white")
        lbl_hired.place(x=10, y=370)
        txt_hired = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_hired_location)
        txt_hired.place(x=150, y=370, width=200)

        lbl_status = Label(Frame1, text="Status", font=("times new roman", 15, "normal"), bg="white")
        lbl_status.place(x=370, y=370)
        txt_contact = Entry(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black", textvariable=self.var_status)
        txt_contact.place(x=510, y=370, width=200)

        # ---------Row7
        lbl_address = Label(Frame1, text="Address", font=("times new roman", 15, "normal"), bg="white")
        lbl_address.place(x=10, y=420)
        self.txt_address = Text(Frame1, font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        self.txt_address.place(x=150, y=420, width=560, height=150)

        # ===========Frame 2 ==============

        # -----------Variables-----------
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.basic_salary = StringVar()
        self.total_days = StringVar()
        self.absent = StringVar()
        self.medical = StringVar()
        self.provident_fund = StringVar()
        self.convince = StringVar()
        self.net_salary = StringVar()

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
        txt_month = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.var_month)
        txt_month.place(x=65, y=70, width=100)

        lbl_year = Label(Frame2, text="Year", font=("times new roman", 14, "normal"), bg="white")
        lbl_year.place(x=165, y=70)
        txt_year = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.var_year)
        txt_year.place(x=207, y=70, width=100)

        lbl_basic_salary = Label(Frame2, text="Basic Salary", font=("times new roman", 14, "normal"), bg="white")
        lbl_basic_salary.place(x=305, y=70)
        txt_basic_salary = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.basic_salary)
        txt_basic_salary.place(x=405, y=70, width=100)

        # ---------Row2
        lbl_total_days = Label(Frame2, text="Total Days", font=("times new roman", 14, "normal"), bg="white")
        lbl_total_days.place(x=10, y=120)
        txt_total_days = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.total_days)
        txt_total_days.place(x=100, y=120, width=150)

        lbl_absent = Label(Frame2, text="Absents", font=("times new roman", 14, "normal"), bg="white")
        lbl_absent.place(x=270, y=120)
        txt_absent = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.absent)
        txt_absent.place(x=340, y=120, width=150)

        # ---------Row3
        lbl_medical = Label(Frame2, text="Medical", font=("times new roman", 14, "normal"), bg="white")
        lbl_medical.place(x=10, y=170)
        txt_medical = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.medical)
        txt_medical.place(x=100, y=170, width=100)

        lbl_provident_fund = Label(Frame2, text="Provident Fund", font=("times new roman", 14, "normal"), bg="white")
        lbl_provident_fund.place(x=215, y=170)
        txt_provident_fund = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.provident_fund)
        txt_provident_fund.place(x=340, y=170, width=150)

        # ---------Row4
        lbl_convince = Label(Frame2, text="Convince", font=("times new roman", 14, "normal"), bg="white")
        lbl_convince.place(x=10, y=220)
        txt_convince = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.convince)
        txt_convince.place(x=100, y=220, width=100)

        lbl_net_salary = Label(Frame2, text="Net Salary", font=("times new roman", 14, "normal"), bg="white")
        lbl_net_salary.place(x=215, y=220)
        txt_net_salary = Entry(Frame2, font=("times new roman", 14, "normal"), bg="lightgray", fg="black", textvariable=self.net_salary)
        txt_net_salary.place(x=340, y=220, width=150)

        # ----------Buttons
        btn_calculate = Button(Frame2, text="Calculate", font=("times new roman", 15, "normal"), bg="#bfc418", fg="black", command=self.calculate)
        btn_calculate.place(x=170, y=265, width=100, height=30)
        btn_save = Button(Frame2, text="Save", font=("times new roman", 15, "normal"), bg="#32a852", fg="white")
        btn_save.place(x=280, y=265, width=100, height=30)
        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_clear.place(x=390, y=265, width=100, height=30)

        # ===========Frame 3 ==============
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=750, y=390, width=520, height=310)

        # ----------Calculater Frame-------------
        self.var_text = StringVar()
        self.var_operator = ""
        def btn_num_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_text.set(self.var_operator)
            print(num)

        def calculate_result():
            res = str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator = ''

        def btn_clear():
            self.var_operator = ''
            self.var_text.set('')

        cal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        cal_Frame.place(x=5, y=5, width=270, height=290)

        txt_result = Entry(cal_Frame, font=("times new roman", 20, "normal"), bg="lightgray", fg="black", textvariable=self.var_text, justify=RIGHT)
        txt_result.place(x=4, y=5, width=260, height=50)

        # ----------Row1---------
        btn_7 = Button(cal_Frame, text="7", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(7))
        btn_7.place(x=5, y=62, width=60, height=50)

        btn_8 = Button(cal_Frame, text="8", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(8))
        btn_8.place(x=70, y=62, width=60, height=50)

        btn_9 = Button(cal_Frame, text="9", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(9))
        btn_9.place(x=135, y=62, width=60, height=50)

        btn_divide = Button(cal_Frame, text="/", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click('/'))
        btn_divide.place(x=200, y=62, width=60, height=50)

        # ----------Row2---------
        btn_4 = Button(cal_Frame, text="4", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(4))
        btn_4.place(x=5, y=116, width=60, height=50)

        btn_5 = Button(cal_Frame, text="5", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(5))
        btn_5.place(x=70, y=116, width=60, height=50)

        btn_6 = Button(cal_Frame, text="6", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(6))
        btn_6.place(x=135, y=116, width=60, height=50)

        btn_multiply = Button(cal_Frame, text="*", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click('*'))
        btn_multiply.place(x=200, y=116, width=60, height=50)

        # ----------Row3---------
        btn_1 = Button(cal_Frame, text="1", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(1))
        btn_1.place(x=5, y=170, width=60, height=50)

        btn_2 = Button(cal_Frame, text="2", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(2))
        btn_2.place(x=70, y=170, width=60, height=50)

        btn_3 = Button(cal_Frame, text="3", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(3))
        btn_3.place(x=135, y=170, width=60, height=50)

        btn_subtract = Button(cal_Frame, text="-", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click('-'))
        btn_subtract.place(x=200, y=170, width=60, height=50)

        # ----------Row4---------
        btn_0 = Button(cal_Frame, text="0", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click(0))
        btn_0.place(x=5, y=225, width=60, height=50)

        btn_dot = Button(cal_Frame, text="C", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_clear())
        btn_dot.place(x=70, y=225, width=60, height=50)

        btn_add = Button(cal_Frame, text="+", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=lambda : btn_num_click("+"))
        btn_add.place(x=135, y=225, width=60, height=50)

        btn_equal = Button(cal_Frame, text="=", font=("times new roman", 15, "normal"), bg="lightgray", fg="black", command=calculate_result )
        btn_equal.place(x=200, y=225, width=60, height=50)

        # ----------Salary Receipt Frame-------------
        salary_receipt_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        salary_receipt_Frame.place(x=280, y=5, width=225, height=290)

        lbl_salary_receipt = Label(salary_receipt_Frame, text="Salary Receipt", font=("times new roman", 20, "bold"), bg="white", fg="black")
        lbl_salary_receipt.place(x=20, y=10)

        # --------- Frame
        salary_receipt_detail_frame = Frame(salary_receipt_Frame, bg="white", bd=2, relief=RIDGE)
        salary_receipt_detail_frame.place(x=5, y=50, width=210, height=185)

        scroll_y = Scrollbar(salary_receipt_detail_frame, orient=VERTICAL)
        scroll_y.pack(fill="y", side=RIGHT)

        self.salary_receipt_text = Text(salary_receipt_detail_frame, font=("times new roman", 12, "normal"), bg="lightgray", fg="black", yscrollcommand=scroll_y.set)
        self.salary_receipt_text.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.salary_receipt_text.yview)

        # ---------Row1
        btn_print = Button(salary_receipt_Frame, text="Print", font=("times new roman", 15, "normal"), bg="lightgray", fg="black")
        btn_print.place(x=115, y=245, width=100, height=30)

    def calculate(self):
        print(self.var_emp_code.get())
        print(self.var_designation.get())
        print(self.var_doj.get())
        print(self.var_name.get())
        print(self.var_dob.get())
        print(self.var_age.get())
        print(self.var_experience.get())
        print(self.var_gender.get())
        print(self.var_proof_id.get())
        print(self.var_email.get())
        print(self.var_contact.get())
        print(self.var_hired_location.get())
        print(self.var_status.get())
        print(self.txt_address.get('1.0', END))

        print(self.var_month.get())
        print(self.var_year.get())
        print(self.basic_salary.get())
        print(self.total_days.get())
        print(self.absent.get())
        print(self.medical.get())
        print(self.provident_fund.get())
        print(self.convince.get())
        print(self.net_salary.get())



win = Tk()
employeeSystem = EmployeeSystem(win)
win.mainloop()