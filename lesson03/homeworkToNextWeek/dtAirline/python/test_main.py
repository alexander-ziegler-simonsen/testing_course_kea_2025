from main import doStuff, airportData
import pytest
from datetime import datetime

departure1 = airportData(datetime(2025, 9, 15, 10, 0), "USA")
destination1 = airportData(datetime(2025, 9, 16, 15, 30), "India")

departure2 = airportData(datetime(2025, 9, 18, 8, 45), "Germany")
destination2 = airportData(datetime(2025, 9, 20, 12, 0), "France")


@pytest.mark.parametrize("age,departure, destination, timeStayingAtLocation, forvented", [
(5, departure1, destination1, 7, 0),
(25, departure2, destination2, 3, 40),
(1, departure1, destination2, 10, 100),
(17, departure2, destination1, 6, 0),
])
def test_positive_DoStuff(age,departure, destination, timeStayingAtLocation, forvented):
    assert doStuff(age, departure, destination, timeStayingAtLocation) == forvented, "string" 
