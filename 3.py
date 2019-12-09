def read_input():
    f = open('3.in')
    return [line.split(',') for line in f.readlines()]


def get_coords(lst):
    points = {}
    x, y, s = 0, 0, 0
    for i in range(len(lst)):
        dirn = lst[i][0]
        for _ in range(int(lst[i][1:])):
            if dirn == 'U':
                y += 1
            elif dirn == 'R':
                x += 1
            elif dirn == 'D':
                y -= 1
            elif dirn == 'L':
                x -= 1

            p = (x, y)
            points[p] = s
            s += 1
    return points


def p1(l1, l2):
    l1_points = get_coords(l1)
    l2_points = get_coords(l2)

    intersections = [x for x in l1_points if x in l2_points]
    print (min([abs(x[0]) + abs(x[1]) for x in intersections]))


def p2(l1, l2):
    l1_points = get_coords(l1)
    l2_points = get_coords(l2)

    intersections = [x for x in l1_points if x in l2_points]
    print (min([l1_points[i] + l2_points[i] for i in intersections]) + 2)


lines = read_input()
p1(lines[0], lines[1])
p2(lines[0], lines[1])
