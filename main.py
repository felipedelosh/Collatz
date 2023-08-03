"""
FelipdelosH
2023

Representates in axis X step to aplicate form / Y eN  

"""
from tkinter import *
from tkinter import ttk
from controller import *


class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self._w = 1080
        self._h = 600
        self.screem = Tk()
        self.canvas = Canvas(self.screem, bg=self.controller.defaultColor['bg'])
        self.lblInsertNumber = Label(self.canvas, fg=self.controller.defaultColor['fg'], bg=self.controller.defaultColor['bg'], text="Insert number:")
        self.txtInsertNumber = Entry(self.canvas, width=20, bg=self.controller.defaultColor['bg'], fg=self.controller.defaultColor['fg'])
        self.btnCalculate = Button(self.canvas, text="CALCULATE", command=self.calculate)
        self.lblOutput = Label(self.canvas, text=self.controller.output)
        self._comboBoxTypeView = StringVar()
        self.ttkComboBoxTypeView = ttk.Combobox(self.canvas, state='readonly', textvariable=self._comboBoxTypeView)
        self.ttkComboBoxTypeView['values'] = self.controller._typesOfGraphics
        self.paintAndShow()


    def paintAndShow(self):
        self.screem.title("3x+1 By FelipedelosH")
        self.screem.geometry(str(self._w)+"x"+str(self._h))
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas.place(x=0, y=0)
        self.lblInsertNumber.place(x=self._w*0.02, y=self._h*0.021)
        self.txtInsertNumber.place(x=self._w*0.1, y=self._h*0.021)
        self.btnCalculate['bg'] = self.controller.defaultColor['visible']
        self.ttkComboBoxTypeView.place(x=self._w*0.23, y=self._h*0.021)
        self.btnCalculate.place(x=self._w*0.38, y=self._h*0.02)
        self.lblOutput.place(x=self._w*0.02, y=self._h*0.94)
        
        self.screem.mainloop()


    def calculate(self):
        number = self.txtInsertNumber.get()
        if self.isValidNumber(number):
            self.controller.setNumber(number)
            self.controller.ejecuteAlgorithm()
            self.updateView()
        else:
            print("Eroorr")

    def updateView(self):
        self.controller.paintRoute(self._comboBoxTypeView.get(), self.canvas)
        self.lblOutput['text'] = self.controller.output


    def isValidNumber(self, number):
        try:
            if int(number) >= 0:
                return True
        except:
            pass
            
        return False


s = Software()
