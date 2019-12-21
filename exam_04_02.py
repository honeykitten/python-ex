numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    elif inp == 'sum' :
        break
    elif inp == 'max' :
        break
    elif inp == 'min' :
        break
    elif inp == 'avr' :
        break
    elif inp == 'sort' :
        break
    elif inp == 'print' :
        print(numlist)
    elif inp == 'len' :
        print(len(numlist))
    else :
        value = float(inp)
        numlist.append(value)
    sum_result = sum(numlist)
    max_result = max(numlist)
    min_result = min(numlist)
    avr_result = sum(numlist) / len(numlist)
    sort_result = sorted(numlist, reverse=True)

if inp == 'sum' :
    print('Sum: ', sum_result)
elif inp == 'max' :
    print('Max: ', max_result)
elif inp == 'min' :
    print('Min: ', min_result)
elif inp == 'avr' :
    print('Average: ', avr_result)
elif inp == 'sort' :
    print('Sort: ', sort_result)
