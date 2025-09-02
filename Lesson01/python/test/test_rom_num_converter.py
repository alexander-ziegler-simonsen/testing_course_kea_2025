from rom_num_converter import roman_num_converter

# tests needed for this function
## check all the rules are right
## check edge cases
### check what happens when you add a letter, that is not on the list
### (not written yet) check what will happen if, we add a input that is not a string (like bool, int or float)

def test_converter_with_1867():
    assert roman_num_converter("MDCCCLXVII") == "1867", "should be 1867"

def test_convert_with_substract_94():
    assert roman_num_converter("XCIV") == "94", "should be 94"


# catches 
def test_convert_catch_over_max():
    assert roman_num_converter("MMMDCMXCIX") == "over max value", "should be 'over max value'"

def test_convert_catch_wrong_letter():
    assert roman_num_converter("XVIYTREQAPU") == "unkown input letters", "should be 'unkown input letters'"

def test_convert_catch_repeated_V():
    assert roman_num_converter("VVII") == "Too many V", "should be 'Too many V'"

def test_convert_catch_repeated_D():
    assert roman_num_converter("DDII") == "Too many D", "should be 'Too many D'"

def test_convert_catch_repeated_L():
    assert roman_num_converter("LLII") == "Too many L", "should be 'Too many L'"

def test_convert_catch_4I():
    assert roman_num_converter("VIIII") == "the count of I,X,C or M went over 3", "should be 'the count of I,X,C or M went over 3'"

def test_convert_catch_4X():
    assert roman_num_converter("MXXXX") == "the count of I,X,C or M went over 3", "should be 'the count of I,X,C or M went over 3'"

def test_convert_catch_4C():
    assert roman_num_converter("MCCCC") == "the count of I,X,C or M went over 3", "should be 'the count of I,X,C or M went over 3'"

def test_convert_catch_4M():
    assert roman_num_converter("MMMMI") == "the count of I,X,C or M went over 3", "should be 'the count of I,X,C or M went over 3'"