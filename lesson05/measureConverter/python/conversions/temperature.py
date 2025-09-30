
from enum import Enum
from decimal import Decimal, ROUND_HALF_UP
class temperatureType(Enum):
    C = 'Celsius'
    K = 'Kelvin'
    F = 'Fahrenheit'

class convertAction(Enum):
    CTOK = 'convert Celsius to Kelvin'
    CTOF = 'convert Celsius to Fahrenheit'
    KTOC = 'convert Kelvin to Celsius'
    KTOF = 'convert Kelvin to Fahrenheit'
    FTOC = 'convert Fahrenheit to Celsius'
    FTOK = 'convert Fahrenheit to Kelvin'

def cToF(value: float):
    return round((value * (9 / 5) + 32), 2)

def cToK(value: float):
    return round((value + 273.15), 2)

def fToC(value: float):
    return round(((value - 32) * (5 / 9)), 2)

def fToK(value: float):
    return round(((value - 32) * (5 / 9) + 273.15), 2)

def kToC(value: float):
    output = ( Decimal(value) - Decimal(273.15) )
    return float(output.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

def kToF(value: float):
    output = ((Decimal(value) - Decimal(273.15)) * Decimal(9/5)) + Decimal(32)
    return float(output.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

class temperatureClass:
    def __init__(self, value: float, whatType: temperatureType):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        self.value = round(float(value), 2)

        if not isinstance(whatType, temperatureType):
            raise ValueError("'whatType' must be of type 'temperatureType'")
        self.whatType = whatType
    
    def convert(self, targetTempType: temperatureType):
        CurrentAction: convertAction
        
        # one of the only way I found to get the switch logic to work in python
        if(self.whatType == temperatureType.C and targetTempType == temperatureType.K):
            CurrentAction = convertAction.CTOK
        elif(self.whatType == temperatureType.C and targetTempType == temperatureType.F):
            CurrentAction = convertAction.CTOF
        elif(self.whatType == temperatureType.K and targetTempType == temperatureType.F):
            CurrentAction = convertAction.KTOF
        elif(self.whatType == temperatureType.K and targetTempType == temperatureType.C):
            CurrentAction = convertAction.KTOC
        elif(self.whatType == temperatureType.F and targetTempType == temperatureType.K):
            CurrentAction = convertAction.FTOK
        elif(self.whatType == temperatureType.F and targetTempType == temperatureType.C):
            CurrentAction = convertAction.FTOC

        match CurrentAction:
            case convertAction.KTOC:
                return kToC(self.value)
            case convertAction.KTOF:
                return kToF(self.value)
            case convertAction.FTOC:
                return fToC(self.value)
            case convertAction.FTOK:
                return fToK(self.value)
            case convertAction.CTOF:
                return cToF(self.value)
            case convertAction.CTOK:
                return cToK(self.value)
        

    