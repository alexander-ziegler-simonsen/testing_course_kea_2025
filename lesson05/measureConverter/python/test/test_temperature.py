import pytest
from conversions.temperature import cToF, cToK, kToC, kToF, fToC, fToK


@pytest.mark.parametrize("fahrenheit, expected", [
    (32, 0),
    (212, 100),
    (98.6, 37),
    (0, -17.78),
    (-40, -40),
])
def test_f_to_c(fahrenheit, expected):
    assert fToC(fahrenheit) == expected


@pytest.mark.parametrize("fahrenheit, expected", [
    (32, 273.15),
    (212, 373.15),
    (98.6, 310.15),
    (0, 255.37),
    (-40, 233.15),
])
def test_f_to_k(fahrenheit, expected):
    assert fToK(fahrenheit) == expected


@pytest.mark.parametrize("celsius, expected", [
    (0, 273.15),
    (100, 373.15),
    (-273.15, 0),
    (25, 298.15),
    (-40, 233.15),
])
def test_c_to_k(celsius, expected):
    assert cToK(celsius) == expected


@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
    (37, 98.6),
    (25, 77),
])
def test_c_to_f(celsius, expected):
    assert cToF(celsius) == expected


@pytest.mark.parametrize("kelvin, expected", [
    (273.15, 32),
    (373.15, 212),
    (310.15, 98.6),
    (255.372, 0),
    (233.15, -40),
])
def test_k_to_f(kelvin, expected):
    assert kToF(kelvin) == expected


@pytest.mark.parametrize("kelvin, expected", [
    (273.15, 0),
    (373.15, 100),
    (0, -273.15),
    (298.15, 25),
    (233.15, -40),
])
def test_k_to_c(kelvin, expected):
    assert kToC(kelvin) == expected
