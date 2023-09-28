smallest = None
print("Before", smallest)
for itervar in [3, 56, 12, 56, 88, 2, 7] :
  if smallest is None :
    smallest = itervar
  elif itervar < smallest :
    smallest = itervar
  print("Loop:", smallest, itervar)
print("Smallest:", smallest)
