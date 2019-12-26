# Counting Pattern
counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Co unts', counts)



jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
# ['chuck', 'fred', 'jan']
print(jjj.keys())
# dict_keys(['chuck', 'fred', 'jan'])
print(jjj.values())
# dict_values([1, 42, 100])
print(jjj.items())
# dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])

for aaa,bbb in jjj.items() :
    print(aaa, bbb)


# Find bigword
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.itmes() :
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)