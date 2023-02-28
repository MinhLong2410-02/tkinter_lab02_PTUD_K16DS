from tkinter import *
import datetime
from tkcalendar import Calendar, DateEntry

class AgeCalc:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Age Calculator")
        self.window.geometry('600x300')
        self.window.resizable(0, 0)
        
        self.head_tilte = Label(self.window, text = 'Age Calculator', 
                                font=('Arial', 23, 'bold','italic', 'underline'), 
                                fg = 'green')
        self.head_tilte.pack()
        
        self.dob = datetime.date.today()
        self.given_day = datetime.date.today()
        
        self.frame = Frame(self.window)
        self.frame.pack()
        Label(self.frame, text = 'Date of Birth: ', font=('Arial', 12)).grid(row = 0, column = 0)
        Label(self.frame, text = 'Given Day: ', font=('Arial', 12)).grid(row = 0, column = 5)
        
        self.dob_entry = DateEntry(self.frame, width=20, background='darkblue',
                        foreground='white', date_pattern='dd/mm/yyyy', font=('Arial', 12))
        self.dob_entry.set_date(self.dob)
        
        self.given_day_entry = DateEntry(self.frame, width=20, background='darkblue',
                        foreground='white', date_pattern='dd/mm/yyyy', font=('Arial', 12))
        self.given_day_entry.set_date(self.given_day)
        self.dob_entry.grid(row = 1, column = 0)
        self.given_day_entry.grid(row = 1, column = 5)
        
        self.caculate_btn = Button(self.frame, text = 'Caculate', font=('Arial', 12), 
                                   foreground='green', background='lightgreen',
                                    command = self.caculate_age)
        self.caculate_btn.grid(row = 4, column = 2, columnspan = 2)
        
        self.result_frame = Frame(self.window, background='gray')
        self.result_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
    
    
    def caculate_age(self):
        self.dob = self.dob_entry.get_date()
        self.given_day = self.given_day_entry.get_date()
        
        age = self.given_day - self.dob
        years, remainder = divmod(age.days, 365)
        months, days = divmod(remainder, 30)
        
        self.result = Label(self.result_frame, text = f'{days} day(s), {months} month(s), {years} year(s)', 
                            font=('Arial', 12), background='gray', foreground='white')
        self.result.grid(row = 0, column = 0, padx=10, pady=10)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AgeCalc()
    app.run()