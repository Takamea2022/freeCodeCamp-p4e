temp = 38
cel = 0

try:
  fahr = float(temp)
except:
  print("Error, code: ")
  quit()
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel) 