p = int(input('Price:\n'))
ac = '0%'
if p > 1000:
  ac = '10%'
elif p > 500:
  ac = '5%'
elif p > 100:
  ac = '3%'
print(ac)