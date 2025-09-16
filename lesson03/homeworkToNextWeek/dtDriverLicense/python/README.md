# driver license notes

the program is about the 2 test every driver need to take.

info :
- point range is between 0 and 100 - theoretical
- numbers of error (int from 0 and up) - practical test
- the driver most take both rxams.
- the driver gets a license, when they meet these conditions:
- - scored >= 85 points on the theoretical test
- - errors are <= 2 
- if the driver fails one of the exams, they have to repeat it.
- both exams failed , means they have to take additinonal hours of driving lessons.

tree notes:
- (t-test) are points at 85 or higher ?
- (p-test) are errrors less then or at 2 ?
- passed t-test?
- passed p-test?


# Decision Table

rule1 - failed both test , extra hours
rule2 - passed driving
rule3 - passed 
rule4 - passed both

| **Conditions** | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| -------------- | ------ | ------ | ------ | ------ |
| Points ≥ 85?   | F      | F      | T      | T      |
| Errors ≤ 2?    | F      | T      | F      | T      |
| **Actions**    |        |        |        |        |
| Passed t-test? | No     | No     | Yes    | Yes    |
| Passed p-test? | No     | Yes    | No     | Yes    |

# black box testing

here i write tests, where i have no knowledge of the code