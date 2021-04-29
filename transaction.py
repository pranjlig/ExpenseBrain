from tkinter import *
from tkinter import ttk
import database


class Transaction:
    def __init__(self, table_name):

        self.table = table_name
        self.window = Tk()
        self.window.title("Transactions")
        self.window.minsize(1050, 700)

        money = PhotoImage(file="images/1618160929241.png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money, anchor="nw")

        self.Table_Frame = Frame(bd=4, relief=RIDGE, bg="white")
        self.Table_Frame.place(x=150, y=50, width=800, height=600)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        back_image = PhotoImage(file="images/1618084232561 (1).png")
        self.back_button = Button(cursor="hand2", image=back_image, highlightthickness=0, width=120, height=70, text="Back", fg="white", font=("Times New Roman", 14, "bold"), compound="center", command=self.window.destroy)
        self.back_button.place(x=0, y=0)

        self.s = ttk.Style()
        self.Transaction_table = ttk.Treeview(self.Table_Frame, column=("id", "date", "category", "amount", "balance", "income"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.make_transaction_table()

        self.window.mainloop()

    def make_transaction_table(self):
        connection = database.connect()
        self.s.theme_use("clam")
        self.s.configure("Treeview.Heading", background="lawngreen", foreground='white', font=('Arial', 13, 'bold'))
        self.s.configure("Treeview", background="lavender", rowheight=35, fieldbackground="lavender", font=('Arial', 11))
        self.s.map('Treeview', background=[('selected', 'darkgray')])
        self.scroll_x.config(command=self.Transaction_table.xview)
        self.scroll_y.config(command=self.Transaction_table.yview)

        self.Transaction_table.heading("id", text="ID", anchor="center")
        self.Transaction_table.heading("date", text="DATE", anchor="center")
        self.Transaction_table.heading("category", text="CATEGORY", anchor="center")
        self.Transaction_table.heading("amount", text="EXPENSE", anchor="center")
        self.Transaction_table.heading("balance", text="BALANCE", anchor="center")
        self.Transaction_table.heading("income", text="INCOME", anchor="center")

        self.Transaction_table['show'] = 'headings'
        self.Transaction_table.column("id", width=100, anchor="center")
        self.Transaction_table.column("date", width=100, anchor="center")
        self.Transaction_table.column("category", width=100, anchor="center")
        self.Transaction_table.column("amount", width=100, anchor="center")
        self.Transaction_table.column("balance", width=100, anchor="center")
        self.Transaction_table.column("income", width=100, anchor="center")

        self.Transaction_table.pack(fill=BOTH, expand=1)
        data = database.get_transaction_table(connection, self.table)

        i = 0
        for row in data:
            self.Transaction_table.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i+1
        self.Transaction_table.pack()
