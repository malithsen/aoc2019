def read_input():
    f = open('1.in')
    return list(f.read().strip().splitlines())

def p1(lst):
    return sum(map(lambda x: x//3-2, lst))

def p2(lst):
    a = 0
    for n in lst:
        f = n//3 - 2
        a += f
        while f > 0:
            f = f//3 - 2
            if f > 0:
                a += f
    return a

lst = list(map(int, read_input()))
print (p1(lst))
print (p2(lst))
