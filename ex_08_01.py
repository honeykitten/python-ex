han = open('./files/mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        # print('Ignore')
        continue
    print(wds[2])