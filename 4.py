from re import finditer

ordered = []
def print_ordered(number, x, k): 
    global ans
    if (k == 0):
        ordered.append(number)
        return
    for i in range( x, 10): 
        print_ordered(number * 10 + i, i, k - 1)

def gen_ordered(k): 
    print_ordered(0, 0, k) 

def has_double(i):
    return any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', i))

k = 6
gen_ordered(k)

p1 = []
p2 = []
for i in ordered:
    if i < 234208 or i > 765869: continue
    str_i = str(i)
    for j in range(len(str_i)-1):
        if str_i[j] == str_i[j+1]:
            p1.append(i)
            break


for i in p1:
    if has_double(str(i)):
        p2.append(i)

#  print (p1)
print (len(p1))
print (p2)
print (len(p2))
