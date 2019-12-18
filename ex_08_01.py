han = open('./files/mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        # print('Ignore')
        continue
    print(wds[2])