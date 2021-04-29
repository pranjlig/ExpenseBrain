from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
import database


class Expense:
    def __init__(self, table_name):
        self.date = ""
        self.amount = ""
        self.selected_category = ""
        self.text = ""
        self.table = table_name

        self.window = Tk()
        self.window.title("Expense")
        self.window.minsize(975, 650)

        money_image = PhotoImage(file="images/1618160612011.png")
        self.canvas = Canvas(height=650, width=975, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money_image, anchor="nw")

        self.date_label = self.canvas.create_text(360, 170, fill="white", text="Date        : ", font=("Arial", 17, "bold"))
        self.amount_label = self.canvas.create_text(360, 230, fill="white", text="Amount   : ", font=("Arial", 17, "bold"))
        self.category_label = self.canvas.create_text(360, 290, fill="white", text="Category : ", font=("Arial", 17, "bold"))
        self.note_label = self.canvas.create_text(360, 350, fill="white", text="Note        : ", font=("Arial", 17, "bold"))

        self.date_entry = DateEntry(self.canvas, width=27, font=("Arial", 10, "bold"), fg="darkslategray")
        self.date_entry.place(x=440, y=161)
        self.amount_entry = Entry(self.canvas, width=30, font=("Arial", 10, "bold"), fg="darkslategray")
        self.amount_entry.place(x=440, y=221)
        self.note_text = Text(height=2, fg="darkslategray", width=30, font=("Arial", 10, "bold"))
        self.note_text.place(x=440, y=341)

        self.variable = StringVar(self.canvas)
        self.category_combobox = ttk.Combobox(self.canvas, textvariable=self.variable, width=27, state='readonly', font=("Arial", 10, "bold"))
        self.category_combobox['values'] = ("Travel", "Grocery", "Entertainment", "Bills", "Laundry", "Eating out", "Shopping", "House Help", "Others")
        self.category_combobox.place(x=440, y=277)

        save_image = PhotoImage(file="images/sign_up100.png")
        self.save_button = Button(cursor="hand2", image=save_image, text="Save", height=50, width=160, compound="center", fg="white", font=("Times New Roman", 17, "bold"), highlightthickness=0, command=self.save_values)
        self.save_button.place(x=410, y=430)
        back_image = PhotoImage(file="images/1618084232561 (1).png")
        self.back_button = Button(cursor="hand2", image=back_image, highlightthickness=0, height=80, text="Back", fg="white", font=("Times New Roman", 14, "bold"), compound="center", command=self.window.destroy)
        self.back_button.place(x=0, y=0)

        self.window.mainloop()

    def save_values(self):
        self.date = self.date_entry.get_date()
        self.amount = self.amount_entry.get()
        self.selected_category = self.variable.get()
        self.text = self.note_text.get("1.0", END)
        if self.amount == "":
            messagebox.showinfo(title="Error", message="Please enter amount.")
        elif self.date == "" or self.date == "Select date from the calendar.":
            messagebox.showinfo(title="Error", message="Please select today's date.")
        elif self.selected_category == "Categories":
            messagebox.showinfo(title="Error", message="Please select a category.")
        else:
            connection = database.connect()
            if not database.add_expense(connection, self.table, str(self.date), self.amount, self.selected_category):
                messagebox.showinfo(title="Unsuccessful", message="Please add an income for this month.")
            else:
                messagebox.showinfo(title="Successful", message="Expense added.☑")
            self.amount_entry.delete(0, END)
            self.variable.set("Categories")
            self.note_text.delete("1.0", END)
