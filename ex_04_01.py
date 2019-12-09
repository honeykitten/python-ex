hour = input('Enter Hours: ')
rate = input('Enter Rate: ' )

hour = float(hour)
rate = float(rate)

if hour >= 41:
    pay = (hour - 40) * rate * 1.5 + 40 * rate
else:
    pay = hour * rate

print('Pay:',pay)