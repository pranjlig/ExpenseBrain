from tkinter import *
from tkinter import messagebox
import database


class SignUp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sign up")
        self.window.minsize(750, 500)

        money_image = PhotoImage(file="images/1618160929231.png")
        self.canvas = Canvas(height=500, width=750, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money_image, anchor="nw")

        self.username_label = self.canvas.create_text(260, 170, fill="white", text="Username : ", font=("Arial", 17, "bold"))
        self.password_label = self.canvas.create_text(260, 230, fill="white", text="Password : ", font=("Arial", 17, "bold"))

        self.username_entry = Entry(self.canvas, fg="darkslategray", width=35, font=("Arial", 10, "bold"))
        self.username_entry.focus()
        self.username_entry.place(x=340, y=161)
        self.password_entry = Entry(self.canvas, fg="darkslategray", width=35, font=("Arial", 10, "bold"))
        self.password_entry.place(x=340, y=221)

        signup_image = PhotoImage(file="images/sign_up100.png")
        self.signup_button = Button(cursor="hand2", image=signup_image, text="SIGN UP", height=50, width=160, compound="center", fg="white", font=("Times New Roman", 17, "bold"), highlightthickness=0, command=self.sign_up_pressed)
        self.signup_button.place(x=290, y=310)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.username, self.password = "", ""
        self.is_closed = False

        self.window.mainloop()

    def sign_up_pressed(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        if self.username == "" or self.password == "":
            messagebox.showinfo(title="Unsuccessful", message="Please fill all the entries.")
        else:
            connection = database.connect()
            if database.username_exists(connection, self.username):
                messagebox.showinfo(title="Unsuccessful", message="This username is taken. Please try another.")
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
            else:
                messagebox.showinfo(title="Successful", message="Done.☑")
                self.window.destroy()

    def on_closing(self):
        self.is_closed = True
        self.window.destroy()
