import tkinter
from tkinter.constants import *
from tkinter import BooleanVar, StringVar, IntVar
from tkinter.ttk import *

class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("500x350")
        self.title("Tkinter Password Generator 🔒")

        self.controller = controller
        self.bind('<Return>', self.controller.handleGenerateButton)

        #---- Variables ----
        self.varNumber = BooleanVar()
        self.varUppercase = BooleanVar()
        self.varLowercase = BooleanVar()
        self.varSymbol = BooleanVar()
        self.varLength = IntVar()
        self.varPwd = StringVar()

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.grid(pady=(500, 0))
        self.mainframe.pack()
        
        self._createFrame()
        self._createCheckbox()
        self._createFrameGenerateBar()

        
    def _createFrame(self):
        self.createFrame = Frame(self.mainframe)
        labelTitle = Label(self.createFrame, text='Password Generator', font=('bold', 20))
        labelTitle.pack(pady=10)
        self.createFrame.pack()


    def _createCheckbox(self):
        self.frameCheckbox = Frame(self.mainframe)
        checkboxNumber = Checkbutton(self.frameCheckbox, text='Numbers (123)', variable=self.varNumber, onvalue=1, offvalue=0, command=self.controller.updateGUI)
        checkboxUppercase = Checkbutton(self.frameCheckbox, text='Uppercase letters (ABC)', variable=self.varUppercase, onvalue=1, offvalue=0, command=self.controller.updateGUI)
        checkboxLowercase = Checkbutton(self.frameCheckbox, text='Lowercase letters (abc)', variable=self.varLowercase, onvalue=1, offvalue=0,  command=self.controller.updateGUI)
        checkboxSymbol = Checkbutton(self.frameCheckbox, text='Randomised symbols (!#$)', variable=self.varSymbol, onvalue=1, offvalue=0,  command=self.controller.updateGUI)
        
        checkboxNumber.grid(row=0, column=0, pady=5, sticky=W)
        checkboxUppercase.grid(row=1, column=0, pady=5, sticky=W)
        checkboxLowercase.grid(row=2, column=0, pady=5, sticky=W)
        checkboxSymbol.grid(row=3, column=0, pady=5, sticky=W)
        self.frameCheckbox.pack()

        
    def _createFrameGenerateBar(self):
        self.frameGenerateBar = Frame(self.mainframe)
        self.labelPwdLength = Label(self.frameGenerateBar, text='Password Length: ')
        self.entryInput = Entry(self.frameGenerateBar, textvariable=self.varLength)
        self.buttonGenerate = Button(self.frameGenerateBar, text="GENERATE", command=self.controller.handleGenerateButton)
        self.labelPwd = Label(self.frameGenerateBar, text='Password: ')
        self.entryPwd = Entry(self.frameGenerateBar, textvariable=self.varPwd)
        self.buttonCopy = Button(self.frameGenerateBar, text="COPY", command=self.controller.copyClipboard)
        
        self.labelPwdLength.grid(row=0, column=0, pady=5, sticky=W)
        self.entryInput.grid(row=0, column=1, pady=5, sticky=E)
        self.buttonGenerate.grid(row=1, column=1, pady=5, sticky=E)
        self.labelPwd.grid(row=2, column=0, pady=5, sticky=W)
        self.entryPwd.grid(row=2, column=1, pady=5, sticky=E)
        self.buttonCopy.grid(row=3, column=1, pady=5, sticky=E)
        
        self.frameGenerateBar.pack(pady=5)
        
          
    def main(self):
        self.mainloop()