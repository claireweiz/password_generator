import string
import random
from view.view import View
from tkinter import messagebox
import pyperclip

class Controller:
    
    def __init__(self) -> None:
        self.view = View(self)
        self.updateGUI()
    
    
    def main(self):
        self.view.main()

    
    def updateGUI(self):
        varPwd = ''
        varLength = self.view.varLength.get() # length of password
        varLength = int(varLength)
        for i in range(varLength): # how many options of format and random them
            generator = []
            if self.view.varNumber.get() == 1: #checkbox number
                generator += str(random.choice(string.digits))
            if self.view.varUppercase.get() == 1: #checkbox uppercase
                generator += random.choice(string.ascii_uppercase)
            if self.view.varLowercase.get() == 1: #checkbox lowercase
                generator += random.choice(string.ascii_lowercase)
            if  self.view.varSymbol.get() == 1: #checkbox symbol
                generator += random.choice(string.punctuation)
            varPwd = varPwd + random.choice(generator)
        
        self.view.varPwd.set(varPwd)
    
    def handleGenerateButton(self):
        anyChecked = self.view.varNumber.get() | self.view.varUppercase.get() | self.view.varLowercase.get() | self.view.varSymbol.get()
        if not anyChecked:
            messagebox.showerror('Error', 'At least one condition needs to be selected.')
        elif self.view.varLength.get() <= 3:
            messagebox.showerror('Error', 'Password length is 4 digits minimum.') 
        else:
            self.updateGUI()
            
        
    def copyClipboard(self):
        pyperclip.copy(self.view.varPwd.get())
               