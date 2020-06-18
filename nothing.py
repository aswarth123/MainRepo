example = set()
example.add(42)
example.add(42.54)
example.add('Hi there')
example.add(True)

nl = lambda: print("")


for i in example:
    print(i)

example.discard(42)

nl()



for i in example:
    print(i)

print(type(nl()))