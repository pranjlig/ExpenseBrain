from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import database
import charts
import datetime as dt


class Analysis:
    def __init__(self, table_name):
        self.table = table_name
        self.window = Tk()
        self.window.title("Analysis")
        self.window.minsize(1050, 700)

        money = PhotoImage(file="images/1618160929241.png")
        self.canvas = Canvas(height=700, width=1050, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = self.canvas.create_image(0, 0, image=money, anchor="nw")

        self.graph_canvas = Canvas(height=430, width=555, highlightthickness=0)
        self.graph_canvas.pack(fill="both", expand=True)
        self.graph_canvas.place(x=270, y=85)

        green_button_image = PhotoImage(file="images/1618083819797 (1).png")
        self.bar_graph_button = Button(cursor="hand2", image=green_button_image, text="Bar Graph", width=154, height=40, compound="center", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, command=self.make_bar)
        self.bar_graph_button.place(x=365, y=570)
        self.pie_chart_button = Button(cursor="hand2", image=green_button_image, text="Pie Chart", width=154, height=40, compound="center", fg="white", font=("Arial", 15, "bold"), highlightthickness=0, command=self.make_pie)
        self.pie_chart_button.place(x=569, y=570)
        back_image = PhotoImage(file="images/1618084232561 (1).png")
        self.back_button = Button(cursor="hand2", image=back_image, highlightthickness=0, height=80, text="Back", fg="white", font=("Times New Roman", 14, "bold"), compound="center", command=self.back_pressed)
        self.back_button.place(x=0, y=0)

        self.make_pie()

        self.window.protocol("WM_DELETE_WINDOW", self.back_pressed)

        self.window.mainloop()

    def make_bar(self):
        connection = database.connect()
        bargraph = database.get_bar(connection, dt.datetime.now().strftime("%m"), dt.datetime.now().strftime("%Y"), self.table)
        charts.bar(bargraph)
        plt.savefig("images/mygraph.png", dpi=400, bbox_inches="tight")
        self.view()

    def make_pie(self):
        connection = database.connect()
        piegraph = database.get_pie(connection, dt.datetime.now().strftime("%m"), dt.datetime.now().strftime("%Y"), self.table)
        charts.pie(piegraph)
        plt.savefig("images/mygraph.png", dpi=400, bbox_inches="tight")
        self.view()

    def view(self):
        self.img = Image.open("images/mygraph.png")

        self.image = self.img.resize((555, 430), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.image)

        self.c = self.graph_canvas.create_image(0, 0, image=self.bg, anchor="nw")
        return self.c

    def back_pressed(self):
        plt.close()
        self.window.destroy()
        plt.close()
