# Exercise 5 'X-DSPAM-Confidence: 0.8475'
str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
piece = str[ipos+2:]
# print(piece)
value = float(piece)
print(value)