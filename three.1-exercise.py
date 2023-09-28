

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hrs)
fr = float(rate)
# print(fh, fr)
if fh > 40 :
  print("Overtime")
  reg = fr * fh
  otp = (fh - 40.0) * (fr * 0.5)
  print(reg, "x", otp)
  xp = reg + otp
else:
  print("Regular")
  xp = fh * fr
print("Pay:", xp) 

