d = {1: "Cây", 2: "Đất", 3: "Nước", 4: "Lửa", 5: "Sắt"}
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
ddd = {"C": 1, "D": 2, "N": 3, "L": 4, "S": 5}
l = {1: "I", 2: "II", 3: "III"}


def countCards(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d[i] + " " + l[j]]
    print(", ".join(p))


def textcountCards(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d[i] + " " + l[j]]
    return ", ".join(p)


def countCard(deck, type):
    p = []
    for j in range(1, 4):
        if deck.count((type, j)) != 0:
            p += [str(deck.count((type, j))) + " " + d[i] + " " + l[j]]
    return ", ".join(p)


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


def ACTION():
    global action
    action = int(
        input(
            "[1] Xuất quân         | [2] Bố trí phòng tuyến | [3] Kích hoạt phòng tuyến |\n[4] Kiểm tra lãnh thổ | [5] Bị tấn công        | [0] Hoãn binh             | => "
        )
    )
    ENTER()
    checkAction()


def checkAction():
    global action
    while action == 2 and lguard and rguard:
        print("Bạn không thể thêm quân vào vị trí phòng tuyến nữa!")
        ENTER()
        ACTION()

    while action == 3 and not lguard and not rguard:
        print("Bạn chưa có quân ở phòng tuyến!")
        ENTER()
        ACTION()

    while action == 5 and not territory:
        print("Bạn không thể bị tấn công khi chưa có quân trên lãnh thổ!")
        ENTER()
        ACTION()


def ENTER():
    print()


print(" " + "-" * 99)
print("|" + "NGŨ HÀNH ĐẠI CHIẾN".center(99) + "|")
print(" " + "-" * 99)
ENTER()
s = input("Mã trận đấu: ")
a = []
for c in s:
    a += [dd[c]]
n = int(input("Số lượng người chơi: "))
m = int(input("Thứ tự lượt chơi của bạn: ")) - 1
while m < 0 or m >= n:
    m = int(input("Vui lòng nhập lại thứ tự chơi của bạn: ")) - 1
ENTER()

print("[QUÂN CỦA BẠN]".rjust(101, "-"))
ENTER()
countCards(a[5 * m : 5 * (m + 1)])
ENTER()
print("[BẮT ĐẦU LƯỢT 1]".rjust(101, "-"))
ENTER()

deck = 5 * n + m
count = 2
hand = a[5 * m : 5 * (m + 1)]
territory = []
lguard = []
rguard = []

while True:
    print(" " + "-" * 99)
    print(
        "|"
        + (
            "Đạo quân của bạn có tổng cộng "
            + str(
                sum(
                    [
                        sum(j * hand.count((i, j)) for j in range(1, 4))
                        for i in range(1, 6)
                    ]
                )
            )
            + " năm kinh nghiệm chiến đấu"
        ).center(99)
        + "|"
    )
    print("|" + "-" * 99 + "|")
    for i in range(1, 6):
        x = str(sum(j * hand.count((i, j)) for j in range(1, 4)))
        print(
            "|"
            + (x + " " + d[i]).center(49)
            + "|"
            + countCard(hand, i).center(49)
            + "|"
        )
        print("|" + "-" * 99 + "|")

    print(
        "|"
        + "Phòng tuyến trái".center(24)
        + "|"
        + (["Chưa có", textcountCards(lguard)][len(lguard) != 0]).center(24)
        + "|"
        + "Phòng tuyến phải".center(24)
        + "|"
        + (["Chưa có", textcountCards(rguard)][len(rguard) != 0]).center(24)
        + "|"
    )
    print(" " + "-" * 99 + " ")
    ENTER()

    ACTION()

    if action == 1:
        s = int(
            input(
                "Mục đích xuất quân: [1] Bảo vệ lãnh thổ | [2] Tấn công đối thủ | => "
            )
        )
        ENTER()
        if s == 1:
            t = input("Chọn quân để bảo vệ lãnh thổ: ").upper()
            ENTER()
        else:
            t = input("Chọn quân để tấn công đối thủ: ").upper()
            ENTER()
        card = []
        for c in t.split():
            card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        while any([x not in hand for x in card]):
            t = input(
                "Quân bạn đã chọn không sẵn sàng!\nVui lòng chọn lại quân khác: "
            ).upper()
            ENTER()
            card = []
            for c in t.split():
                card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        if s == 1:
            print("Quân bạn đã chọn để bảo vệ lãnh thổ là: ", end="")
            countCards(card)
            ENTER()
            territory += card
        else:
            print("Quân bạn đã chọn để tấn công đối thủ là: ", end="")
            countCards(card)
            ENTER()
            t = int(input("Kết quả trận đánh: [1] Thắng | [2] Thua | => "))
            ENTER()
            if t == 1:
                territory += card
        for c in card:
            hand.remove(c)

    elif action == 2:
        s = input("Chọn quân vào vị trí phòng tuyến: ").upper()
        ENTER()
        card = []
        for c in s.split():
            card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        while any([x not in hand for x in card]):
            s = input(
                "Quân bạn đã chọn không sẵn sàng!\nVui lòng chọn lại quân khác: "
            ).upper()
            ENTER()
            card = []
            for c in s.split():
                card += [(ddd[c[1]], int(c[2]))] * int(c[0])
        for c in card:
            hand.remove(c)
        if lguard:
            print("Quân bạn đã chọn vào vị trí phòng tuyến phải là: ", end="")
            rguard = card
        else:
            print("Quân bạn đã chọn vào vị trí phòng tuyến trái là: ", end="")
            lguard = card
        countCards(card)
        ENTER()

    elif action == 3:
        if lguard:
            print("Phòng tuyến trái: ", end="")
            countCards(lguard)
        else:
            print("Phòng tuyến trái: Chưa có")
        if rguard:
            print("Phòng tuyến phải: ", end="")
            countCards(rguard)
        else:
            print("Phòng tuyến phải: Chưa có")
        ENTER()
        s = int(
            input(
                "[1] Kích hoạt phòng tuyến trái | [2] Kích hoạt phòng tuyến phải | => "
            )
        )
        ENTER()
        while (s == 1 and not lguard) or (s == 2 and not rguard):
            print("Bạn chưa có quân phòng tuyến " + ["trái!", "phải!"][s - 1])
            ENTER()
            s = int(
                input(
                    "[1] Kích hoạt phòng tuyến trái | [2] Kích hoạt phòng tuyến phải | => "
                )
            )
            ENTER()
        if s == 1:
            print("Đã kích hoạt phòng tuyến trái là: ", end="")
            countCards(lguard)
            territory += lguard
            lguard = []
        if s == 2:
            print("Đã kích hoạt phòng tuyến phải là: ", end="")
            countCards(rguard)
            territory += rguard
            rguard = []
        ENTER()

    elif action == 4:
        print(" " + "-" * 99)
        print(
            "|"
            + (
                "Bạn đã có đạo quân "
                + str(
                    sum(
                        [
                            sum(j * territory.count((i, j)) for j in range(1, 4))
                            for i in range(1, 6)
                        ]
                    )
                )
                + " năm kinh nghiệm trên lãnh thổ"
            ).center(99)
            + "|"
        )
        print("|".ljust(100, "-") + "|")
        y = ""
        for i in range(1, 6):
            x = str(sum(j * territory.count((i, j)) for j in range(1, 4)))
            y += "|" + (x + " " + d[i]).center(19)
        print(y + "|")
        print(" " + "-" * 99)
        ENTER()

    elif action == 5:
        s = input("Binh chủng bị thương vong là: ").upper()
        print("Binh chủng " + d[ddd[s]] + " đã không còn trên lãnh thổ!")
        territory = [x for x in territory if x[0] != ddd[s]]
        ENTER()

    if action not in [3, 4, 5]:
        print(("[BẮT ĐẦU LƯỢT " + str(count) + "]").rjust(101, "-"))
        ENTER()
        print("Viện binh")
        drawOneCard(a[deck])
        ENTER()
        hand += [a[deck]]
        deck += n
        count += 1
        if deck >= 60:
            print("Đã hết quân chi viện!")
