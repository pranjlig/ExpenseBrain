from tkinter import *
from tkinter import messagebox
import database


class LogIn:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.minsize(1050, 700)
        
        money_plant = PhotoImage(file="images/micheile-henderson-ZVprbBmT8QA-unsplash (2).png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money_plant, anchor="nw")
        
        self.username_label = self.canvas.create_text(680, 300, anchor="nw", fill="white", text="Username : ", font=("Arial", 15, "bold"))
        self.password_label = self.canvas.create_text(680, 350, anchor="nw", fill="white", text="Password : ", font=("Arial", 15, "bold"))
        self.account_label = self.canvas.create_text(680, 500, anchor="nw", text="Don't have an account? ", font=("Arial", 10, "bold"))
        
        self.username_entry = Entry(self.canvas, width=30, fg="darkslategray", font=("Arial", 10, "bold"))
        self.username_entry.focus()
        self.username_entry.place(x=800, y=300)
        self.password_entry = Entry(self.canvas, width=30, show="*", fg="darkslategray", font=("Arial", 10, "bold"))
        self.password_entry.place(x=800, y=350)
        
        login_image = PhotoImage(file="images/1618083819790 (1).png")
        self.login_button = Button(cursor="hand2", image=login_image, text="LOG IN", compound="center", fg="white", font=("Times New Roman", 15, "bold"), highlightthickness=0, height=50, width=128, command=self.login_pressed)
        self.login_button.place(x=780, y=400)
        signup_image = PhotoImage(file="images/24949-1-sign-up-button-transparent-image (1).png")
        self.signup_button = Button(cursor="hand2", image=signup_image, highlightthickness=0, height=35, width=120, command=self.sign_up_pressed)
        self.signup_button.place(x=840, y=480)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.is_closed = False
        self.sign_up = False
        self.login = False
        self.create_homepage = False
        self.table_name = ""

        self.window.mainloop()

    def sign_up_pressed(self):
        self.window.destroy()
        self.sign_up = True

    def login_pressed(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showinfo(title="Unsuccessful", message="Please fill all the entries.")
        else:
            connection = database.connect()
            if not database.check_username(connection, username):
                messagebox.showinfo(title="Unsuccessful", message="User does not exist.")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
            else:
                value = database.check_password(connection, username, password)
                if value == "False":
                    messagebox.showinfo(title="Unsuccessful", message="Incorrect password.")
                    self.password_entry.delete(0, END)
                else:
                    self.window.destroy()
                    self.sign_up = False
                    self.create_homepage = True
                    self.table_name = value

    def on_closing(self):
        if messagebox.askokcancel(title="Quit", message="Do you want to quit?"):
            self.is_closed = True
            self.window.destroy()
