from dataclasses import dataclass
from datetime import datetime

# airline

# values needed
# person(age), destination(date, location/contry), departure(date, location/contry), stayingTime

# maybe add later 
# more people one one trip
# return trip

@dataclass
class airportData:
    datetime: datetime
    contry: str

def checkIfRule1(age:int, destination: airportData):
    if(age > 18 and destination.contry == "India" and (destination.datetime.weekday != 0 and destination.datetime.weekday != 4)):
        return True
    else:
        return False
    

def checkIfRule2(departure: airportData, destination: airportData):
    if(destination.contry != "India" and (departure.datetime.weekday != 0 and departure.datetime.weekday != 4)):
        return True
    else:
        return False

def checkIfRule3(timeStayingAtLocation:int):
    if(timeStayingAtLocation >= 6):
        return True
    else:
        return False

def checkIfRule4(age:int):
    if( 2 < age > 18):
        return True
    else:
        return False

def checkIfRule5(age:int, departure: airportData, destination: airportData):
    if(age <= 2):
        return True
    else:
        return False

def doStuff(age:int, departure: airportData, destination: airportData, timeStayingAtLocation:int):
    check1 = checkIfRule1(age, destination)
    check2 = checkIfRule2(departure, destination)
    check3 = checkIfRule3(timeStayingAtLocation)
    check4 = checkIfRule4(age)
    check5 = checkIfRule5(age, departure, destination)

    if(check5):
        return 100
    elif(check4 and check3):
        return 50
    elif(check4):
        return 40
    elif(check2 and check3):
        return 35
    elif(check2):
        return 25
    elif(check1):
        return 20
    else:
        return 0
