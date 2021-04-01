import random

a = []

for i in range(70):
    n = random.randint(0, 5)
    m = random.randint(1, 3)
    p = random.randint(0, 9)
    while (n == 0 and a.count((n, p)) == 1) or (
        n != 0
        and (
            (m == 1 and a.count((n, m)) == 6)
            or (m == 2 and a.count((n, m)) == 4)
            or (m == 3 and a.count((n, m)) == 2)
        )
    ):
        n = random.randint(0, 5)
        m = random.randint(1, 3)
        p = random.randint(0, 9)
    if n == 0:
        a += [(n, p)]
    else:
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
    # Song chủng
    (0, 0): "F",
    (0, 1): "G",
    (0, 2): "H",
    (0, 3): "I",
    (0, 4): "J",
    (0, 5): "K",
    (0, 6): "L",
    (0, 7): "M",
    (0, 8): "N",
    (0, 9): "O"
    # # Biến chủng
    # (0, 10): "P",
    # (0, 11): "Q",
    # (0, 12): "R",
    # (0, 13): "S",
    # (0, 14): "T",
    # (0, 15): "U",
    # (0, 16): "V",
    # (0, 17): "W",
    # (0, 18): "X",
    # (0, 19): "Y",
}

print("Mã của bộ bài là: ")
for c in a:
    print(end=d[c])

