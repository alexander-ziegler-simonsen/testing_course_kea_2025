
# info for both projects
I use UV to run this project and Pytest is the test runner of my chose.

I run pytest with this command:

```bash
uv run pytest
```

## pytest notes
- in order for pytest to find the test files, they need to start with "test_" followed by the full-file-name that needs to be tested.
- how to write in asserts in pytest (it uses python's build in assert)
- - assert doStuff() == "x", "message given if failed"
- each test is showed as a green dot '.' if it passed or a red "F" if it failed

# Roman Numerals converter
The files
- rom_num_converter.py
- test_rom_num_converter.py

## notes
I only needed to handle 3 values to do all the logic in the main loop:
- previousValue
- currentNum
- nextNum
The 3 variables are saved as numbers, after the letter-key was given to the global dist (dictionary) 'roman_numerals' and the key-value was returned.

The 'roman_num_converter' function first check the text input and sees if it follows the rules set.
If the input is okay, the function go through each char in the text input.

The first time the function loops, it checks if the first char is a positive or negative value (IV = 4) by comparing it with the next char, then add/remove the first char value from the total output.

After the first loop the function do 3 checks
- is the current number the same as the last one ? (add)
- is the current number bigger or the same as the next number? (add)
- is the current number smaller than the next one ? (remove)

When the function is done, it makes a final check to see if the output value have gone over the max allowed value. Each of these validation checks return a string message of what went wrong.

If everything check didn't find any errors, the output will be returned as the full total count in a string format.



# simple calculator
The files
- calculator.py
- test_calculator.py


