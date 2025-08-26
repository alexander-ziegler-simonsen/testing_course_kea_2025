
roman_numerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

non_repeat = [ "V", "L", "D" ]              # `V, L, D` cannot be repeated
only_allowed_negative = [ "I", "X", "C" ]   # only `I, X, C` can be used as subtractive
max_3_sequentially = [ "I", "X", "C", "M" ] # `I, X, C, M` can be repeated up to 3 times consecutively (e.g., 4 is `IV`, not `IIII`)
max_value = "MMMCMXCIX"                     # max value 'MMMCMXCIX' = 3999


def roman_num_converter(roman_value):
    return 404