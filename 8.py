def read_input():
    f = open('8.in')
    return list(map(int, f.read().strip()))

def p1(lst):
    size = 25*6
    least_zeros = 100000
    ans = 0
    layers = []
    for i in range(0, len(lst), size):
        layer = lst[i:i+size]
        zeros = layer.count(0)
        if zeros < least_zeros:
            least_zeros = zeros
            ans = layer.count(1) * layer.count(2)
        layers.append(layer)
    return ans, layers

def p2(layers):
    size = 25*6
    image = [next(filter(lambda x: x != 2, layer)) for layer in zip(*layers)]
    for i in range(0, len(image), 25):
        row = ''.join(['#' if x == 1 else ' ' for x in image[i:i+25]])
        print (row)

lst = read_input()
p1_ans, layers = p1(lst)
print (p1_ans)

p2(layers)
