def computepay(hours, rate) :
  print("In computepay", hours, "x", rate)
  if hours > 40 :
    reg = rate * hours
    otp = (hours - 40.0) * (rate * 0.5)
    pay = reg + otp
  else:
    pay = hours * rate
  print("Returning", pay)
  return pay


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hrs)
fr = float(rate)

xp = computepay(fh, fr)

print("Pay:", xp)35