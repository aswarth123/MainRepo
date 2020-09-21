def IsPrime(num):
    """Checks if it is prime or not"""
    checker = None
    if num > 2:
        for i in range(2, num):
            if (num%i == 0):
                checker = False
                break                
            else:
                checker = True
    elif num==2:
        checker = True
    else:
        checker = False
    return(checker)

f = open('numbers.txt', "a")

num = input('Give me the number: ')
a = int(num)
ds = '-' + str(a) + str(IsPrime(a)) + '-' + "\n"

f.write(ds)
f.close()
