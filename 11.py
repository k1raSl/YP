class Calculation:
    def __init__(self, initial_value=""):
        self.__calculationLine = initial_value

    SetCalculationLine = lambda self, value: setattr(self, '_Calculation__calculationLine', value)
    SetLastSymbolCalculationLine = lambda self, symbol: setattr(self, '_Calculation__calculationLine',
                                                                self.__calculationLine + symbol)
    GetCalculationLine = property(lambda self: self.__calculationLine)
    GetLastSymbol = property(lambda self: self.__calculationLine[-1] if self.__calculationLine else "")
    DeleteLastSymbol = lambda self: setattr(self, '_Calculation__calculationLine', self.__calculationLine[:-1])

calc = Calculation()

calc.SetCalculationLine("123+456")
print("CalculationLine:", calc.GetCalculationLine)  

calc.SetLastSymbolCalculationLine("=")
print("После добавления '=':", calc.GetCalculationLine)  

print("Последний символ:", calc.GetLastSymbol)  

calc.DeleteLastSymbol()
print("После удаления последнего символа:", calc.GetCalculationLine)
