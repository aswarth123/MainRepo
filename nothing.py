example = set()
example.add(42)
example.add(42.54)
example.add('Hi there')
example.add(True)

example2 = set()
example2.add(43)
example2.add(43.54)
example2.add('Hello there')
example2.add(False)

nl = lambda: print("")


for i in example:
    print(i)

example.discard(42)

nl()



for z in example2:
    print(z)

print(type(nl()))
