
'''

Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:


Input: 

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...


Output :

franky

sinatra123


'''

import re

with open('text_q3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\S+@\S+'

match = re.findall(pattern, text)

# control block to see the matches
print(match)

# to get the each email address
for i in match:

    # to split from '@' charachter and get first part
    print(i.split('@')[0]) 