from tkinter import *
from math import sqrt, pow

class Calculator():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.icon()
        self.displayed_button()

    def icon(self):
        # Navbar icon
        self.navbaricon = PhotoImage(file="navbar.png")
        self.button_nav = Button(root, image=self.navbaricon)
        self.button_nav.place(x=0, y=0)
        # History icon
        self.historical_icon = PhotoImage(file="hisICON.png")
        self.button_historical_calculator = Button(root, image=self.historical_icon, command=self.History)
        self.button_historical_calculator.place(x=360, y=6)

        # Type of calculator
        self.label_type_of_Calculator = Label(root, text="Scientific", fg="#000000", font=("Time New Romans", 16, "bold"))
        self.label_type_of_Calculator.pack(side=TOP)
        self.label_type_of_Calculator.place(x=50,y=5)

        # Entry
        self.user_entry = Entry(root, width=15, font=("Arial", 35, "bold"), justify=RIGHT )
        self.user_entry.place(x=5, y=70)
        self.user_entry.config(borderwidth=0, relief="flat")

        root.bind("<Return>", self.bind_keys)
            
    def displayed_button(self):
        buttons = [


            'sqrt', 'C', '←','/',
            '7', '8', '9','*',
            '4', '5', '6','+',
            '1', '2', '3','-',
            '0', '=','.','x²',
            
        ]

        row = 2
        col = 0

        for buttonlayout in buttons:
            button = Button(root, text=buttonlayout, padx=15, pady=15, font=("Arial", 24, "bold"))
            button.grid(row=row, column=col, padx=5, pady=5)
            button.config(command= lambda x = buttonlayout: self.button_clicked(x))
            
            
            col += 1
            if col > 3:
                col = 0
                row += 1


    def bind_keys(self, event):
        try:
            result = eval(self.user_entry.get())
            self.user_entry.delete(0, END)
            self.user_entry.insert(0, result)
        except Exception as e:
            self.user_entry.delete(0, END)
            self.user_entry.insert(0, "Error")
        
        

    def button_clicked(self, button):
        current_result = self.user_entry.get()
        if button == "C":
            self.user_entry.delete(0, END)
        elif button == "←":
            self.user_entry.delete(len(current_result) -1)
        elif button == "=":
            try:
                result = eval(self.user_entry.get())
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, result)
            except Exception as e:
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, "Error")
        elif button == "sqrt":
            try:
                result = sqrt(float(self.user_entry.get()))
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, result)
            except ValueError:
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, "Error")
        elif button == "x²":
            try:
                result = pow(float(self.user_entry.get()), 2)
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, result)
            except ValueError:
                self.user_entry.delete(0, END)
                self.user_entry.insert(0, "Error")
        else:
            self.user_entry.insert(END, button)
    
    
 
    def History(self):
        self.history_label = Label(text="there's no history yet" )
        self.history_label.pack()
        # still in codin


if __name__ == "__main__":
    root = Tk()
    root.geometry("404x636")
    photo = PhotoImage(file="cal.png")
    root.iconphoto(True, photo)
    root.rowconfigure(1, weight=1)
    calculator = Calculator(root)
    root.mainloop()
    
