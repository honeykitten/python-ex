list = []
while True:
    inp = input('Enter: ')
    args = inp.split()
    if args[0] == 'done' :
        break
    elif args[0] == 'print' :
        print(list)
    elif args[0] == 'append' :
        list.append(args[1])
    elif args[0] == 'in' :
        if args[1] in list :
            print('True')
        else :
            print('False')
    elif args[0] == 'notin' :
        if args[1] not in list :
            print('True')
        else :
            print('False')
    elif args[0] == 'remove' :
        vv = args[1]
        del list[list.index(vv)]
    elif args[0] == 'appends' :
        newdata = args[1].split(',')
        list = list + newdata
    else :
        print('wrong command!')