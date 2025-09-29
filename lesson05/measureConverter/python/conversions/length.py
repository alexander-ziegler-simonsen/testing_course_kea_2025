
from enum import Enum

class measureType(Enum):
    METRIC = 'Metric'
    IMPERIAL = 'Imperial'

class lengthClass:
    def __init__(self, value: float, whatType: measureType):
        # round to 2 decimal, if it's a number
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        self.value = round(float(value), 2)

        if not isinstance(whatType, measureType):
            raise ValueError("'whatType' must be of type 'measureType'")
        self.whatType = whatType
    
    def convert(self):
        # convert cm to inch
        if(self.whatType == measureType.METRIC):
            return round(self.value * 0.3937007874, 2)
        # convert inch to cm
        else: 
            return round(self.value * 2.54, 2)