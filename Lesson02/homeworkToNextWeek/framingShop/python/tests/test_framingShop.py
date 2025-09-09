import pytest
from app.framingShop import getFramePrice

# positive 

@pytest.mark.parametrize("width, height, expected", [
    (30, 30, 3000),
    (31, 31, 3000),
    (32, 32, 3000),
    (45, 65, 3500),
    (58, 98, 3500),
    (59, 99, 3500),
    (60, 100, 3500),
])
def test_GetFramePriceRangePostive(width, height, expected):
    assert getFramePrice(width, height) == expected

# negative 
@pytest.mark.parametrize("width, height, expected", [
    (28, 30, 0),
    (29, 30, 0),
    (30, 28, 0),
    (30, 29, 0),
    (28, 28, 0),
    (29, 29, 0),
    (61, 30, 0),
    (62, 30, 0),
    (30, 101, 0),
    (30, 102, 0),
    (61, 101, 0),
    (62, 102, 0)
])
def test_GetFramePriceRangeNegative(width, height, expected):
    assert getFramePrice(width, height) == expected