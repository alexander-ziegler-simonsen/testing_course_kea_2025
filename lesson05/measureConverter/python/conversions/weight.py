
from enum import Enum

class weightType(Enum):
    METRIC = 'Metric'
    IMPERIAL = 'Imperial'

class Weight:
    def __init__(self, value: float, whatType: weightType):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        self.value = round(float(value), 2)

        if not isinstance(whatType, weightType):
            raise ValueError("'whatType' must be of type 'weightType'")
        self.whatType = whatType
    
    def convert(self):
        # convert kg to pound
        if(self.whatType == weightType.METRIC):
            return self.value * 2.2046244202
        # convert pound to kg
        else: 
            return self.value * 0.453592