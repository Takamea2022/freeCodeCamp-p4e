import re
# x = 'My 2 favorite numbers are 19 and 42'
x = 'My email address is arante.emmanuel2017@gmail.com'
# y = re.findall('[0-9]+', x)
y = re.findall('\S+@+\S+', x)
print(y)
y = re.findall('[AEIOU]', x)
print(y)

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)