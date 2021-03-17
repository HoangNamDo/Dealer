s = input("Nhập mã của bộ bài: ")
dd = {
    "0": (1, 1),
    "1": (1, 2),
    "2": (1, 3),
    "3": (2, 1),
    "4": (2, 2),
    "5": (2, 3),
    "6": (3, 1),
    "7": (3, 2),
    "8": (3, 3),
    "9": (4, 1),
    "A": (4, 2),
    "B": (4, 3),
    "C": (5, 1),
    "D": (5, 2),
    "E": (5, 3),
}
a = []
for c in s:
    a += [dd[c]]

d = {1: "Cây", 2: "Đất", 3: "Nước", 4: "Lửa", 5: "Sắt"}
ddd = {"c": 1, "d": 2, "n": 3, "l": 4, "s": 5}
l = {1: "I", 2: "II", 3: "III"}


def countCards(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d[i] + " " + l[j]]
    print(", ".join(p) + ".")


def countCard(deck, type):
    p = []
    for j in range(1, 4):
        if deck.count((type, j)) != 0:
            p += [str(deck.count((type, j))) + " " + d[i] + " " + l[j]]
    print(", ".join(p) + ".")


def drawOneCard(card):
    for i in range(7):
        if i == 0 or i == 6:
            print(" " + "-" * 7 + " ")
        elif i == 2:
            print("|" + f"{d[card[0]]:^7}" + "|")
        elif i == 4:
            print("|" + f"{l[card[1]]:^7}" + "|")
        else:
            print("|       |")


n = int(input("Có tất cả bao nhiêu người chơi?: "))
m = int(input("Bạn là người chơi thứ mấy?: ")) - 1
while m < 0 or m >= n:
    m = int(input("Vui lòng nhập lại thứ tự chơi của bạn: ")) - 1


print()
print("-" * 67 + "[BÀI CỦA BẠN]")
print()
countCards(a[5 * m : 5 * (m + 1)])
print()
print("-" * 71 + "[BẮT ĐẦU]")


deck = 5 * n + m
count = 1
hand = a[5 * m : 5 * (m + 1)]
lguard = []
rguard = []

while True:
    print("Bài trên tay: ")
    for i in range(1, 6):
        x = sum(j * hand.count((i, j)) for j in range(1, 4))
        if x:
            print(x, d[i] + ":", end=" ")
            countCard(hand, i)
    if lguard:
        print("Úp trái: ", end="")
        countCards(lguard)
    else:
        print("Úp trái: Chưa có")
    if rguard:
        print("Úp phải: ", end="")
        countCards(rguard)
    else:
        print("Úp phải: Chưa có")
    print()
    action = int(input("[1] Xuất bài | [2] Úp bài | [3] Mở bài | [0] Bỏ lượt | => "))

    while action == 2 and lguard and rguard:
        print("Không thể úp bài thêm nữa!")
        action = int(
            input("[1] Xuất bài | [2] Úp bài | [3] Mở bài | [0] Bỏ lượt | => ")
        )

    while action == 3 and not lguard and not rguard:
        print("Bạn chưa úp bài!")
        action = int(
            input("[1] Xuất bài | [2] Úp bài | [3] Mở bài | [0] Bỏ lượt | => ")
        )

    if action == 1:
        s = input("Chọn bài để xuất: ")
        card = []
        for c in s.split():
            card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        while any([x not in hand for x in card]):
            s = input(
                "Bài bạn chọn không có đủ trên tay! Vui lòng chọn lại bài để xuất: "
            )
            card = []
            for c in s.split():
                card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        print("Bài bạn đã chọn để xuất là: ", end="")
        countCards(card)
        for c in card:
            hand.remove(c)

    if action == 2:
        s = input("Chọn bài để úp: ")
        card = []
        for c in s.split():
            card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        while any([x not in hand for x in card]):
            s = input(
                "Bài bạn chọn không có đủ trên tay! Vui lòng chọn lại bài để úp: "
            )
            card = []
            for c in s.split():
                card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        print("Bài bạn đã chọn để úp là: ", end="")
        countCards(card)
        for c in card:
            hand.remove(c)
        if lguard:
            rguard = card
        else:
            lguard = card

    if action == 3:
        print()
        if lguard:
            print("Úp trái: ", end="")
            countCards(lguard)
        else:
            print("Úp trái: Chưa có")
        if rguard:
            print("Úp phải: ", end="")
            countCards(rguard)
        else:
            print("Úp phải: Chưa có")
        print()
        s = int(input("[1] Mở úp trái | [2] Mở úp phải | => "))
        while (s == 1 and not lguard) or (s == 2 and not rguard):
            print("Bạn chưa có bài úp " + ["trái!", "phải!"][s - 1])
            s = int(input("[1] Mở úp trái | [2] Mở úp phải | => "))
        print()
        if s == 1:
            print("Đã mở úp trái là: ", end="")
            countCards(lguard)
            lguard = []
        if s == 2:
            print("Đã mở úp phải là: ", end="")
            countCards(rguard)
            rguard = []
        print("-" * 80)
        print()

    if action != 3:
        print("Rút bài: ")
        drawOneCard(a[deck])
        hand += [a[deck]]
        print("-" * (64 - len(str(count))) + "[KẾT THÚC LƯỢT " + str(count) + "]")
        print()
        deck += n
        count += 1
        if deck >= 60:
            print("Hết quân bài ngũ hành để rút")
