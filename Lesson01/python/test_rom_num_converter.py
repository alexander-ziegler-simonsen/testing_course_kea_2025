from rom_num_converter import roman_num_converter

# tests needed for this function
## check all the rules are right
### (not written yet) check what will happen if, you have more than one set of add/sub in the same string
### (not written yet) check what will happen if, the order of add/sub is wrong
## check edge cases
### check what happens when you add a letter, that is not on the list
### (not written yet) check what will happen if, we add a input that is not a string (like bool, int or float)

def test_converter_with_1867():
    assert roman_num_converter("MDCCCLXVII") == 1867, "should be 1867"

def test_convert_with_substract_94():
    assert roman_num_converter("XCIV") == 94, "should be 94"


# catches 
def test_convert_catch_over_max():
    assert roman_num_converter("MMMDCMXCIX") == "over max value", "should be 'over max value'"

def test_convert_catch_wrong_letter():
    assert roman_num_converter("XVIYTREQAPU") == "wrong input", "should be 'wrong input'"

def test_convert_catch_4I():
    assert roman_num_converter("VIIII") == "I count went over 3", "should be 'I count went over 3'"

def test_convert_catch_4X():
    assert roman_num_converter("MXXXX") == "X count went over 3", "should be 'X count went over 3'"

def test_convert_catch_4C():
    assert roman_num_converter("MCCCC") == "C count went over 3", "should be 'C count went over 3'"

def test_convert_catch_4M():
    assert roman_num_converter("MMMMI") == "M count went over 3", "should be 'M count went over 3'"