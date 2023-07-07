from Relogio import ClockDisplay
import tkinter as tk

class Clock():
    def __init__(self,root):
        self.root=root
        self.lblClock=tk.Label(root,font=('Arial',26),fg='black')
        self.lblClock.pack()
        self.alteracao()

    def alteracao(self):
        now=number.timeTick()
        self.lblClock['text']=now
        self.root.after(1000,self.alteracao)     

if __name__ == '__main__':
    number=ClockDisplay()
    var=tk.Tk()
    var.title("Cronômetro")
    Clock(var)
    var.mainloop()
