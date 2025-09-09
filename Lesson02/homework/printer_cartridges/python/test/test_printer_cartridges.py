from printer_cartridges import discountCalculation
import pytest


# all values - 5,6,50,98,99,100,101,9999,10000 

@pytest.mark.parametrize("num1, forvented", [
    (5, 0),
    (6, 0),
    (50, 0),
    (98, 0),
    (99, 0),
    (100, 0.2),
    (101, 0.2),
    (9999, 0.2),
    (10000, 0.2)
])
def test_positive_discountCalculation(num1, forvented):
    assert discountCalculation(num1) == forvented, "should be "+str(forvented)

@pytest.mark.parametrize("num1, forvented", [
    (0, (0)),
    (4, (0)),
])
def test_negative_discountCalculation(num1, forvented):
    assert discountCalculation(num1) == forvented, "should be "+str(forvented)

