from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database


class Delete:
    def __init__(self, table_name):

        self.table = table_name
        self.window = Tk()
        self.window.title("Delete Transaction")
        self.window.minsize(1050, 700)

        money = PhotoImage(file="images/1618160929241.png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money, anchor="nw")

        self.Table_Frame = Frame(bd=4, relief=RIDGE, bg="white")
        self.Table_Frame.place(x=225, y=80, width=650, height=400)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.id_label = self.canvas.create_text(390, 530, fill="white", text="ID : ", font=("Arial", 17, "bold"))
        self.id_entry = Entry(self.canvas, width=40, font=("Arial", 10, "bold"), fg="darkslategray")
        self.id_entry.insert(END, string="Select ID of the transaction from the table.")
        self.id_entry.place(x=425, y=521)

        delete_image = PhotoImage(file="images/sign_up100.png")
        self.delete_button = Button(cursor="hand2", image=delete_image, text="Delete", height=50, width=160, compound="center", fg="white", font=("Times New Roman", 17, "bold"), highlightthickness=0, command=self.delete_pressed)
        self.delete_button.place(x=460, y=580)

        back_image = PhotoImage(file="images/1618084232561 (1).png")
        self.back_button = Button(cursor="hand2", image=back_image, highlightthickness=0, width=120, height=70, text="Back", fg="white", font=("Times New Roman", 14, "bold"), compound="center", command=self.window.destroy)
        self.back_button.place(x=0, y=0)

        self.s = ttk.Style()
        self.Transaction_table = ttk.Treeview(self.Table_Frame, column=("id", "date", "category", "amount", "balance", "income"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.make_delete_table()

        self.window.mainloop()

    def make_delete_table(self):
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

        data = database.get_delete_table(connection, self.table)
        i = 0
        for row in data:
            self.Transaction_table.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i+1
        self.Transaction_table.pack()

    def delete_pressed(self):
        id = self.id_entry.get()
        if id == "" or id == "Select ID of the transaction from the table.":
            messagebox.showinfo(title="Unsuccessful", message="Please select id")
        else:
            connection = database.connect()
            is_done = database.delete_transaction(connection, self.table, id)
            if is_done:
                messagebox.showinfo(title="Successful", message="Transaction deleted.☑")
                for i in self.Transaction_table.get_children():
                    self.Transaction_table.delete(i)
                data = database.get_delete_table(connection, self.table)
                i = 0
                for row in data:
                    self.Transaction_table.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                    i = i+1
                self.id_entry.delete(0, END)
            else:
                messagebox.showinfo(title="Unsuccessful", message="Please select a valid id")
                self.id_entry.delete(0, END)
