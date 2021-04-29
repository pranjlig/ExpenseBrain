from tkinter import *
from tkinter import ttk
import database
import datetime as dt


class Savings:

    def __init__(self, table_name):

        self.table = table_name
        self.window = Tk()
        self.window.title("Saving Suggestions")
        self.window.minsize(1050, 700)

        money = PhotoImage(file="images/1618160929241.png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money, anchor="nw")

        self.Table_Frame = Frame(bd=4, relief=RIDGE, bg="white")
        self.Table_Frame.place(x=75, y=150, width=900, height=500)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        back_image = PhotoImage(file="images/1618084232561 (1).png")
        self.back_button = Button(cursor="hand2", image=back_image, highlightthickness=0, width=120, height=70, text="Back", fg="white", font=("Times New Roman", 14, "bold"), compound="center", command=self.window.destroy)
        self.back_button.place(x=0, y=0)

        connection = database.connect()
        data = database.get_data(connection, self.table, dt.datetime.now().strftime("%m"), dt.datetime.now().strftime("%Y"))
        if not data:
            balance = 0
        else:
            balance = data[-1][0]

        self.saving_label = self.canvas.create_text(460, 50, anchor="n", fill="white", text="Current Balance : ", font=("Arial", 20, "bold"))
        self.saving_amount_label = self.canvas.create_text(625, 50, anchor="n", fill="white", text=f"₹ {balance}", font=("Arial", 20, "bold"))

        self.s = ttk.Style()
        self.saving_table = ttk.Treeview(self.Table_Frame, column=("id", "sn", "tenure", "mi", "ir", "return"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.make_saving_table()

        self.window.mainloop()

    def make_saving_table(self):

        connection = database.connect()
        data = database.get_data(connection, self.table, dt.datetime.now().strftime("%m"), dt.datetime.now().strftime("%Y"))

        if not data:
            balance = 0
        else:
            balance = data[-1][0]

        i8 = balance + balance * (8 / 100)
        i73 = balance + balance * (7.3 / 100)
        i7 = balance + balance * (7 / 100)
        i10 = balance + balance * (10 / 100)
        i85 = balance + balance * (8.5 / 100)

        self.s.theme_use("clam")
        self.s.configure("Treeview.Heading", background="lawngreen", foreground='white', font=('Arial', 13, 'bold'))
        self.s.configure("Treeview", background="lavender", rowheight=50, fieldbackground="lavender", font=('Arial', 11))
        self.s.map('Treeview', background=[('selected', 'darkgray')])
        self.scroll_x.config(command=self.saving_table.xview)
        self.scroll_y.config(command=self.saving_table.yview)

        self.saving_table.heading("id", text="ID", anchor="center")
        self.saving_table.heading("sn", text="Scheme Name", anchor="center")
        self.saving_table.heading("tenure", text="Tenure", anchor="center")
        self.saving_table.heading("mi", text="Minimum Investment", anchor="center")
        self.saving_table.heading("ir", text="Interest Rate", anchor="center")
        self.saving_table.heading("return", text="Return", anchor="center")

        self.saving_table['show'] = 'headings'
        self.saving_table.column("id", width=35, anchor="center")
        self.saving_table.column("sn", width=315, anchor="center")
        self.saving_table.column("tenure", width=130, anchor="center")
        self.saving_table.column("mi", width=175, anchor="center")
        self.saving_table.column("ir", width=130, anchor="center")
        self.saving_table.column("return", width=65, anchor="center")

        self.saving_table.pack(fill=BOTH, expand=1)

        lst = [
            (1, 'Public Provident fund (PPF)', '15 years', '₹ 500 per year', '8% p.a.', i8),
            (2, 'National Savings Certificate (NSC)', '5 years', '₹ 100 per year', '8% p.a.', i8),
            (3, 'Post Office Time Deposit', '1 to 5 years', '₹ 200 per year', '7% p.a.', i7),
            (4, 'Post Office Recurring Deposit', '5 years', '₹ 10 per month', '7.3% p.a', i73),
            (5, 'Post Office Monthly Income Scheme (POMIS)', '5 years', '₹ 1500 per year', '7.3 % p.a.', i73),
            (6, 'Fixed Deposit', '7 days to 10 years', 'Rs 100', '6.50% – 7.25% p.a.', i7),
            (7, 'National Pension System (NPS)', 'Until age of 60', '₹ 1000 per year', '9% – 12% p.a.', i10),
            (8, 'Employees Provident Fund (EPF)', '5 years', '12% of monthly salary', '8.5% p.a.', i85),
        ]

        i = 0
        for row in lst:
            self.saving_table.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1

        self.saving_table.pack()
