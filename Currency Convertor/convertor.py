# # Python Project on Currency Converter

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = converter
        self.resizable(False, False)
        self.geometry("700x300")
        self.configure(bg="#FFE873")

        # Label
        self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',20,'bold'))

        self.date_label = Label(self, text = f"Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.config(font=5)

        self.intro_label.place(x = 30, y = 5)
        self.date_label.place(x = 250, y= 80)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.from_label = Label(self, text="From", justify = tk.CENTER,bg = "#FFE873")
        self.from_label.config(font=20)
        self.to_label = Label(self, text="To", justify = tk.CENTER,bg = "#FFE873")
        self.to_label.config(font=20)
        self.amount_field = Entry(self, bd = 3, relief = tk.RIDGE, justify = tk.CENTER, validate='key', validatecommand=valid, font = 15)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, borderwidth = 3)
        self.converted_amount_field_label.config(font=30)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value

        font = ("Courier", 15, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing
        self.from_label.place(x = 70, y = 120)
        self.from_currency_dropdown.place(x = 70, y= 150)
        self.amount_field.place(x = 76, y = 190, width=150, height=35)
        self.to_label.place(x = 450, y = 120)
        self.to_currency_dropdown.place(x = 450, y= 150)
        self.converted_amount_field_label.place(x = 456, y = 190, width=150, height = 35)
        
        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 15, 'bold'))
        self.convert_button.place(x = 290, y = 230)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9]{10}")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()

