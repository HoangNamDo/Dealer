import random

a = []
for i in range(1, 61):
    n = random.randint(1, 5)
    m = random.randint(1, 3)
    while (
        (m == 1 and a.count((n, m)) == 6)
        or (m == 2 and a.count((n, m)) == 4)
        or (m == 3 and a.count((n, m)) == 2)
    ):
        n = random.randint(1, 5)
        m = random.randint(1, 3)
    a += [(n, m)]

d = {
    (1, 1): "0",
    (1, 2): "1",
    (1, 3): "2",
    (2, 1): "3",
    (2, 2): "4",
    (2, 3): "5",
    (3, 1): "6",
    (3, 2): "7",
    (3, 3): "8",
    (4, 1): "9",
    (4, 2): "A",
    (4, 3): "B",
    (5, 1): "C",
    (5, 2): "D",
    (5, 3): "E",
}

print("Mã của bộ bài là: ")
for c in a:
    print(end=d[c])
