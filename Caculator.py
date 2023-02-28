from tkinter import *
    
class Caculator:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Calculator")
        self.window.resizable(0, 0)
        self.number_labels = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1)
        }

        self.digital_labels = {
            "+": (1, 3), "-": (2, 3), "*": (3, 3), "/": (4, 3), '.': (4, 0), '=': (4, 2)
        }
        self.init_object()
        
        
    def create_button(self, text, row, column, command=None):
        button = Button(
            self.window, 
            text=text, 
            font=("verdana", 22), 
            relief=GROOVE, 
            border=0, 
            command=(lambda x = text: self.on_click(text) if command else command)
        )
        button.grid(row=row, column=column, sticky=NSEW)
        return button
    
    def create_number_buttons(self):
        buttons = []
        for number, number_value in self.number_labels.items():
            button = self.create_button(number, number_value[0], number_value[1], 1)
            buttons.append(button)
        return buttons
    
    def create_digital_buttons(self):
        digital_buttons = []
        for digital, digital_value in self.digital_labels.items():
            button = self.create_button(digital, digital_value[0], digital_value[1], 1)
            digital_buttons.append(button)
        return digital_buttons
    
    def create_clear_button(self):
        button = self.create_button("CLEAR", 4, 5, 1)
        return button
        
    def create_expression(self):
        e = Entry(self.window, 
                  width=35,
                  borderwidth=5,
                  font=("verdana", 22), 
                  bg="light grey", 
                  justify=RIGHT,
                  validate='key',
                  validatecommand=(self.window.register(self.validate_entry_input), '%P')
                )
        e.grid(row = 0, column = 0, columnspan=4, padx=10, pady=10)
        return e
    
    def init_object(self):
        self.expression_entry = self.create_expression()
        self.number_buttons = self.create_number_buttons()
        self.digital_buttons = self.create_digital_buttons()
        self.clear_button = self.create_clear_button()
    
    def validate_entry_input(self, new_value):
        allowed_chars = {"+", "-", "*", "/", ".", ""}
        allowed_keysyms = {"Delete", "Left", "Right", "BackSpace"}

        for char in new_value:
            if char not in allowed_chars and not char.isdigit():
                return False
        
        if new_value in allowed_keysyms:
            return True
        
            
        return True
    
    def on_click(self, text):
        text = str(text).strip().lower()
        self.update_entry(text)
    
    def update_entry(self, text):
        if text == 'clear':
            self.expression_entry.delete(0, END)
            self.expression_entry.insert(0, "")
            return 
        expression = self.expression_entry.get()
        if text == '=':
            try:
                text = str(eval(expression))
                self.expression_entry.delete(0, END)    
            except:
                return
        else: 
            expression += text
        self.expression_entry.insert(len(expression)-1, text)
    
    def run(self):
        self.window.mainloop()
        
caculator = Caculator()
caculator.run()
