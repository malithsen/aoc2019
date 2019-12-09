def read_input():
    f = open('5.in')
    return list(map(int, f.read().split(',')))

def get_params(n):
    params = list(str(n))
    # leftpad
    if len(params) < 5:
        for i in range(5-len(params)):
            params.insert(0, "0")
    return list(map(int, params))

def get_val(lst, mode, pos):
    i = lst[pos]
    return lst[i] if mode == 0 else i

def add(lst, params, a, b):
    return get_val(lst, params[2], a) + get_val(lst, params[1], b)

def mult(lst, params, a, b):
    return get_val(lst, params[2], a) * get_val(lst, params[1], b)

def repr(lst, i):
    print (lst[lst[i+1]])

def jmp_true(lst, params, a, b, pc):
    if get_val(lst, params[2], a) != 0:
        return get_val(lst, params[1], b)
    else:
        return pc+3
def jmp_false(lst, params, a, b, pc):
    if get_val(lst, params[2], a) == 0:
        return get_val(lst, params[1], b)
    else:
        return pc + 3

def lt(lst, params, a, b):
    return get_val(lst, params[2], a) < get_val(lst, params[1], b)

def eq(lst, params, a, b):
    return get_val(lst, params[2], a) == get_val(lst, params[1], b)

def compute(lst, inp):
    pc = 0

    while pc < len(lst):
        params = get_params(lst[pc])
        op = params[4]

        if op == 1:
            second = pc+1
            third = pc+2
            result = lst[pc+3]
            lst[result] = add(lst, params, second, third)
            pc += 4
        elif op == 2:
            second = pc+1
            third = pc+2
            result = lst[pc+3]

            lst[result] = mult(lst, params, second, third)
            pc += 4
        elif op == 3:
            lst[lst[pc+1]] = inp
            pc += 2
        elif op == 4:
            repr(lst, pc)
            pc += 2
        elif op == 5:
            second = pc+1
            third = pc+2
            pc = jmp_true(lst, params, second, third, pc)
        elif op == 6:
            second = pc+1
            third = pc+2
            pc = jmp_false(lst, params, second, third, pc)
        elif op == 7:
            second = pc+1
            third = pc+2
            result = lst[pc+3]
            lst[result] = 1 if lt(lst, params, second, third) else 0
            pc += 4
        elif op == 8:
            second = pc+1
            third = pc+2
            result = lst[pc+3]

            lst[result] = 1 if eq(lst, params, second, third) else 0
            pc += 4
        elif op == 99:
            break
        else:
            break

lst = list(map(int, read_input()))
#  compute(lst, 1)
compute(lst, 5)
