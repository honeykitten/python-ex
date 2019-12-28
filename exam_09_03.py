word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1

lst = list(d.keys())
lst.sort()
for key in lst:
    print(key, d[key])

# lst = list(d)
# lst.sort()
# for key in lst:
#     print(key)