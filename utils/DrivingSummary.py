import time
import tkinter as tk
from tkinter import font as tkfont



class DrivingSummary(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        self.configure(background='#67BFFF')
        label = tk.Label(self, text="Driving summary", font=controller.title_font,bg='#67BFFF')
        label.pack(side="top", fill="x", pady=10)

        labelframe1 = tk.LabelFrame(self, text="Hope you enjoyed it",bg='#67BFFF')
        labelframe1.pack(fill="both", expand="yes")

        text_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        toplabel = tk.Label(labelframe1, text="Thank you for visiting and have a lovely day.", font=text_font,bg='#67BFFF')
        toplabel.pack()
        toplabel.place(anchor="c", relx=.5, rely=.5)


        infomessage = tk.Label(labelframe1,text = "If you would like more information please visit:https://driverleics.github.io/",bg='#67BFFF')
        infomessage.pack()

        photo = tk.PhotoImage(file="leicester.gif")
        a1label = tk.Label(labelframe1,image = photo,bg='#67BFFF')
        a1label.image = photo
        a1label.pack()



        button1 = tk.Button(self, text="Back to start menu", command=lambda: controller.show_frame("StartPage"),bg='#FF9A2E')
        button1.focus()
        button1.pack()

        self.bind("<<"+self.__class__.__name__+">>", self._event_call)

    def _event_call(self, event):
        print(self.__class__.__name__)
        print("event -> " + str(event))