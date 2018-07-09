# Regex examples

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group())
# print(mo.groups())

heroRegEx = re.compile(r'Batman|Tina Fey')
mo1 = heroRegEx.search('Batman and Tina Fey.')
mo1.group()

mo2 = heroRegEx.search('Tina Fey and Batman.')
mo2.group()

batRegex = re.compile(r'(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile man lost a wheel')
mo3.group()
# print (mo3.group(1))

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 555-4242')
print (mo4.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo5 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print (mo5)