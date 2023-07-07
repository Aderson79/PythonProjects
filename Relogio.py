class numberDisplay():
    def __init__(self,limit):
        self.__limit=limit
        self.__value=0

    def Incremento(self):
        self.__value=(self.__value+1)%self.__limit

    def getValue(self):
        return self.__value

    def getDisplay(self):
        if(self.__value<10):
            return "0" + str(self.__value)
        else: 
            return "" + str(self.__value)

class ClockDisplay: 
    def __init__(self):
        self.__hora=numberDisplay(24)
        self.__minuto=numberDisplay(60)
        self.__segundos=numberDisplay(60)
        self.__updateDisplay()
        
    def timeTick(self):
        self.__segundos.Incremento()
        if(self.__segundos.getValue()==0):
            self.__minuto.Incremento()
            if(self.__minuto.getValue()==0):
                self.__hora.Incremento()
        return self.__updateDisplay()

    def __updateDisplay(self):
        return self.__hora.getDisplay() + ":" + self.__minuto.getDisplay() + ":" + self.__segundos.getDisplay()    
