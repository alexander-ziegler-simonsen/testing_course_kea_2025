# globals
roman_numerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
non_repeat = [ "V", "L", "D" ]              # `V, L, D` cannot be repeated
only_allowed_negative = [ "I", "X", "C" ]   # only `I, X, C` can be used as subtractive
max_3_sequentially = [ "I", "X", "C", "M" ] # `I, X, C, M` can be repeated up to 3 times consecutively (e.g., 4 is `IV`, not `IIII`)
#max_value = "MMMCMXCIX"                     # max value 'MMMCMXCIX' = 3999

# too many repeats
def checkCharRepeats(textInput, charsToCheck, maxRepeatCount):   
    for char in charsToCheck:
        if(textInput.count(char) > maxRepeatCount):
            return "Too many " + char
        
    return 0

# contain unkown chars
def checkTextInput(textInput, allowedChars):    
    for char in textInput:
        if(not char in allowedChars):
            return "unkown input letters"

    return 0

# more than 3 sequentially repeats
def checkOverSequentiallyMaxrepeats(inputValue, charToCheck, maxRepeatCount):   
    counter = 0
    lastChar = ""
    handlingOneOfTheLetters = False
    for i in range(len(inputValue)):
        #print(str(i) + " | counter : " + str(counter) + " | lastchar : " + lastChar + " | handlingOneOfTheLetters : " + str(handlingOneOfTheLetters))
        
        currentChar = inputValue[i]
        # keep finding more
        if(currentChar in charToCheck and handlingOneOfTheLetters):
            if(lastChar != currentChar):
                counter = 1
                lastChar = currentChar
            else:
                counter += 1
                lastChar = currentChar
        # found one 
        if(currentChar in charToCheck and not handlingOneOfTheLetters):
            lastChar = currentChar
            handlingOneOfTheLetters = True
            counter += 1
        # didn't find one
        if(currentChar not in charToCheck):
            lastChar = currentChar
            counter = 0
            handlingOneOfTheLetters = False
        # if we are over 'maxRepeatCount'
        if(counter > maxRepeatCount):
            return "the count of I,X,C or M went over 3" # maybe should be 'maxRepeatCount'
        
    return 0


def roman_num_converter(roman_value):
    # validation rules
    checkInput = checkTextInput(roman_value, roman_numerals)
    if (checkInput != 0):
        return checkInput
    checkMaxRepeat = checkCharRepeats(roman_value, non_repeat, 1)
    if (checkMaxRepeat != 0):
        return checkMaxRepeat
    checkOver3Repeats = checkOverSequentiallyMaxrepeats(roman_value, max_3_sequentially, 3)
    if (checkOver3Repeats != 0):
        return checkOver3Repeats
    
    output = 0
    previousValue = 0
    # the main logic loop
    for i in range(len(roman_value)):
        # set the values
        currentNum = roman_numerals[roman_value[i]]
        nextI = i+1
        nextNum = 0
        if(nextI < len(roman_value)):
            nextNum = roman_numerals[roman_value[(nextI)]]

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
            elif(currentNum >= nextNum):
                output += currentNum
            elif(currentNum < nextNum):
                output -= currentNum
        
        # overwrite the previousValue value
        previousValue = currentNum
    

    # check if the value is bigger than Max value
    if(output > 3990):
        return "over max value"

    return str(output)

#output = roman_num_converter("MDCCCLXVII")
#print(output)