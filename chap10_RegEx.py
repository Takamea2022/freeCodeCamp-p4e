
#This is called duoble split pattern:
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
piece = email.split('@')
print(piece[1])

# Atposition function
atpos = line.find('@')
print(atpos)

sppos = line.find(' ', atpos)
print(sppos)

host = line[atpos+1 : sppos]
print(host)