from tkinter import *
from tkinter import messagebox
import database
import datetime as dt


class HomePage:
    def __init__(self, table_name):
        self.table = table_name
        self.window = Tk()
        self.window.title("Home page")
        self.window.minsize(1050, 700)

        money = PhotoImage(file="images/1618160929241.png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money, anchor="nw")

        self.month_canvas = Canvas(self.canvas, height=110, width=170, highlightthickness=0, bg="#c0e218")
        self.month_canvas.place(x=0, y=0)
        self.month_canvas.create_text(85, 50, fill="white", text=f"{dt.datetime.now().strftime('%B')}", font=("Arial", 22, "italic bold"))

        black_button_image = PhotoImage(file="images/1618084232561 (2).png")
        self.transaction_button = Button(cursor="hand2", image=black_button_image, bg="black", text="Transaction", fg="white", font=("Arial", 15, "bold"), height=105, width=220, highlightthickness=0, compound="center", command=self.transaction_pressed)
        self.transaction_button.place(x=170, y=0)
        self.analysis_button = Button(cursor="hand2", image=black_button_image, bg="black", text="Analysis", fg="white", font=("Arial", 15, "bold"), height=105, width=220, highlightthickness=0, compound="center", command=self.analysis_pressed)
        self.analysis_button.place(x=390, y=0)
        self.suggestion_button = Button(cursor="hand2", image=black_button_image, bg="black", text="Suggestion", fg="white", font=("Arial", 15, "bold"), height=105, width=220, highlightthickness=0, compound="center", command=self.suggestion_pressed)
        self.suggestion_button.place(x=610, y=0)
        self.delete_button = Button(cursor="hand2", image=black_button_image, bg="black", text="Delete", fg="white", font=("Arial", 15, "bold"), height=105, width=220, highlightthickness=0, compound="center", command=self.delete_pressed)
        self.delete_button.place(x=830, y=0)

        connection = database.connect()
        data = database.get_data(connection, self.table, dt.datetime.now().strftime("%m"), dt.datetime.now().strftime("%Y"))
        if not data:
            balance = 0
            income = 0
        else:
            balance = data[-1][0]
            income = data[-1][1]
        expense = income-balance
        self.income_label = self.canvas.create_text(410, 265, anchor="nw", fill="white", text="Income   : ", font=("Arial", 20, "bold"))
        self.income_amount_label = self.canvas.create_text(550, 265, anchor="nw", fill="white", text=f"₹ {income}", font=("Arial", 20, "bold"))
        self.expense_label = self.canvas.create_text(410, 315, anchor="nw", fill="white", text="Expense : ", font=("Arial", 20, "bold"))
        self.expense_amount_label = self.canvas.create_text(550, 315, anchor="nw", fill="white", text=f"₹ {expense}", font=("Arial", 20, "bold"))
        self.line = self.canvas.create_line(410, 365, 640, 365, fill="grey", width=2)
        self.balance_label = self.canvas.create_text(410, 385, anchor="nw", fill="white", text="Balance  : ", font=("Arial", 20, "bold"))
        self.balance_amount_label = self.canvas.create_text(550, 385, anchor="nw", fill="white", text=f"₹ {balance}", font=("Arial", 20, "bold"))

        green_button_image = PhotoImage(file="images/1618083819797 (1).png")
        self.income_button = Button(cursor="hand2", image=green_button_image, text="+  Income", width=154, height=40, compound="center", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, command=self.income_pressed)
        self.income_button.place(x=370, y=535)
        self.income_button = Button(cursor="hand2", image=green_button_image, text="+  Expense", width=154, height=40, compound="center", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, command=self.expense_pressed)
        self.income_button.place(x=574, y=535)

        self.is_closed = False
        self.income = False
        self.expense = False
        self.transaction = False
        self.analysis = False
        self.suggestion = False
        self.delete = False

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()

    def expense_pressed(self):
        self.window.destroy()
        self.expense = True

    def income_pressed(self):
        self.window.destroy()
        self.income = True

    def transaction_pressed(self):
        self.window.destroy()
        self.transaction = True

    def analysis_pressed(self):
        self.window.destroy()
        self.analysis = True

    def suggestion_pressed(self):
        self.window.destroy()
        self.suggestion = True

    def delete_pressed(self):
        self.window.destroy()
        self.delete = True

    def on_closing(self):
        if messagebox.askokcancel(title="Quit", message="Do you want to quit?"):
            self.is_closed = True
            self.window.destroy()
