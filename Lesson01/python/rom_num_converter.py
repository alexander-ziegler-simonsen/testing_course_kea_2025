
roman_numerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

non_repeat = [ "V", "L", "D" ]              # `V, L, D` cannot be repeated
only_allowed_negative = [ "I", "X", "C" ]   # only `I, X, C` can be used as subtractive
max_3_sequentially = [ "I", "X", "C", "M" ] # `I, X, C, M` can be repeated up to 3 times consecutively (e.g., 4 is `IV`, not `IIII`)
max_value = "MMMCMXCIX"                     # max value 'MMMCMXCIX' = 3999


def roman_num_converter(roman_value):
    # first check if something is wrong

    # too many repeats
    for i in non_repeat:
        if(roman_value.count(i) > 1):
            return "Too many " + i
    
    # contain unkown chars
    for char in roman_value:
        if(not char in roman_numerals):
            return "unkown input letters"
        
    # more than 3 sequentially repeats
    counter = 0
    lastChar = ""
    handlingOneOfTheLetters = False
    for i in range(len(roman_value)):
        #print(str(i) + " | counter : " + str(counter) + " | lastchar : " + lastChar + " | handlingOneOfTheLetters : " + str(handlingOneOfTheLetters))
        
        currentChar = roman_value[i]
        # keep finding more
        if(currentChar in max_3_sequentially and handlingOneOfTheLetters):
            if(lastChar != currentChar):
                counter = 1
                lastChar = currentChar
            else:
                counter += 1
                lastChar = currentChar
        # found one 
        if(currentChar in max_3_sequentially and not handlingOneOfTheLetters):
            lastChar = currentChar
            handlingOneOfTheLetters = True
            counter += 1
        # didn't find one
        if(currentChar not in max_3_sequentially):
            lastChar = currentChar
            counter = 0
            handlingOneOfTheLetters = False
        # if we are over 3
        if(counter > 3):
            return "the count of I,X,C or M went over 3"
    
    output = 0
    previousValue = 0
    # the main logic loop
    for i in range(len(roman_value)):

        # set the values
        currentNum = roman_numerals[roman_value[i]]
        nextI = i+1
        nextII = i+2
        nextNum = 0
        next2Num = 0
        if(nextI < len(roman_value)):
            nextNum = roman_numerals[roman_value[(nextI)]]
        if(nextII < len(roman_value)):
            next2Num = roman_numerals[roman_value[(nextII)]]

        # first time runing 
        if(previousValue == 0):
            # check if the first part is negative or positive
            if(roman_numerals[roman_value[(nextI)]] > currentNum):
                output -= currentNum
            else:
                output += currentNum

        else:

            # if it is the same, add it
            if(currentNum == previousValue):
                output += currentNum
            # if current is bigger than the next, add it
            elif(currentNum > nextNum and next2Num != 0):
                output += currentNum
            elif(currentNum < nextNum and next2Num != 0):
                output -= currentNum
        
        # overwrite the previousValue value
        previousValue = currentNum

    
    # check if the value is bigger than Max value
    if(output > 3990):
        return "over max value"

    return str(output)

# output = roman_num_converter("VIIIIDD")
# print(output)