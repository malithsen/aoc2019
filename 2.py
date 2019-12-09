def read_input():
    f = open('2.in')
    return list(map(int, f.read().split(',')))

def p1(lst, a=12, b=2):
    lst[1] = a
    lst[2] = b
    #  lst = [1,9,10,3,2,3,11,0,99,30,40,50]
    #  print (lst)
    i = 0

    while i < len(lst):
        n = lst[i]
        #  print ('n', n)
        #  print ('lst', lst)
        if n == 1:
            lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
            i += 4
        elif n == 2:
            lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
            i += 4
        elif n == 99:
            break
        else:
            break
    return lst


def p2(lst):
    for i in range(100):
        for j in range(100):
            ans = p1(lst[:], i, j)
            if ans[0] == 19690720:
                print ("p2", 100 * ans[1] + ans[2])

    pass

lst = list(map(int, read_input()))
#  print (p1(lst))
print (p2(lst))
