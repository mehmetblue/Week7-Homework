'''

Question 1:
Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6


'''

import re

# format to search
pattern = '[A-Za-z]{2}[0-9]{1}[A-Za-z]{2}[0-9]{2}[A-Za-z]{1}[0-9]{1}'

# stinrg to searched by pattern
test_stirng = 'AABZA1111AEGTV5YH678MK4FM53B6'

result = re.findall(pattern, test_stirng)

# to showing the result without [] and '' characters
print(result[0])