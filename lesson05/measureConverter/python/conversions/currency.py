import currencyapicom
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("CURRENCY_API_KEY")

print(apiKey)

class Currency:
    def __init__(self, contryLetters):
        self.contryLetters = contryLetters

    def myConvert(self, value):
        clint = currencyapicom.Client(apiKey)
        rounded = round(value, 2)

        result = clint.convert(rounded, None, None, [self.contryLetters])

        print(result)

# for testing
# what = Currency("DKK")
# what.myConvert(100)
    