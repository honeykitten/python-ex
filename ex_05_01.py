number = 0
total = 0
count = 0
while True:
    number = input('Enter: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
        continue
    total = total + number
    count = count + 1

print('Sum:',total)
print('Count:',count)
print('Average:',total/count)