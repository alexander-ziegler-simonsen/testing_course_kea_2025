from calculator import sum, subtract, divide, multiply

def test_sum():
    assert sum(1, 2) == 3, "should be 3"

def test_subtract():
    assert subtract(6,3) == 3, "should be 3"

def test_divide():
    assert divide(9,3) == 3, "should be 3"

def test_multiply():
    assert multiply(1,3) == 3, "should be 3"

# + _ -4 and -5
# - _ -4 and -5
# / _ 7 / 4 , 1,75
# / _ 7 / 0 = 0 