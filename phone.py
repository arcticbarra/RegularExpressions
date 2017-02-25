import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

mo = phoneNumberRegex.search('My number is 115-222-111')
print(f'Phone number found: {mo.group()}')
