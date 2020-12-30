frnds = [0] * 100001
connections = [0] * 100001


def init(n):
    global frnds
    global connections
    for i in range(n + 1):
        frnds[i] = i
        connections[i] = 1
    return


def findGroup(x):
    global frnds
    if frnds[x] == x:
        return x
    frnds[x] = findGroup(frnds[x])
    return frnds[x]


def union(x, y):
    global frnds
    global connections
    x = findGroup(x)
    y = findGroup(y)
    if x != y:
        if connections[y] > connections[x]:
            x, y = y, x
        connections[x] += connections[y]
        frnds[y] = x
    return connections[x]


def main():
    t = int(input())

    while t > 0:
        t -= 1
        n = int(input())

        init(min(n * 2, 100000))
        name_id = {}
        sz = 0

        for i in range(n):
            names = input().split()
            f1, f2 = names

            if f1 not in name_id:
                sz += 1
                name_id[f1] = sz
            id_f1 = name_id[f1]

            if f2 not in name_id:
                sz += 1
                name_id[f2] = sz
            id_f2 = name_id[f2]

            print(union(id_f1, id_f2))
    return


if __name__ == "__main__":
    main()

'''
Sample Input
1
3
Fred Barney
Barney Betty
Betty Wilma
Sample Output
2
3
4
'''
