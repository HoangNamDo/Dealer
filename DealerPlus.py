d1 = {1: "Cây", 2: "Đất", 3: "Nước", 4: "Lửa", 5: "Sắt"}
d2 = {
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
    # Song chủng
    "F": (0, 0),
    "G": (0, 1),
    "H": (0, 2),
    "I": (0, 3),
    "J": (0, 4),
    "K": (0, 5),
    "L": (0, 6),
    "M": (0, 7),
    "N": (0, 8),
    "O": (0, 9)
    # # Biến chủng
    # "P": (0, 10),
    # "Q": (0, 11),
    # "R": (0, 12),
    # "S": (0, 13),
    # "T": (0, 14),
    # "U": (0, 15),
    # "V": (0, 16),
    # "W": (0, 17),
    # "X": (0, 18),
    # "Y": (0, 19),
}
d3 = {"C": 1, "D": 2, "N": 3, "L": 4, "S": 5}
l = {1: "I", 2: "II", 3: "III"}
k1 = {
    0: "Cây|Đất",
    1: "Cây|Nước",
    2: "Cây|Lửa",
    3: "Cây|Sắt",
    4: "Đất|Nước",
    5: "Đất|Lửa",
    6: "Đất|Sắt",
    7: "Nước|Lửa",
    8: "Nước|Sắt",
    9: "Lửa|Sắt"
    # 10: "Cây>",
    # 11: "Đất>",
    # 12: "Nước>",
    # 13: "Lửa>",
    # 14: "Sắt>",
    # 15: ">Cây",
    # 16: ">Đất",
    # 17: ">Nước",
    # 18: ">Lửa",
    # 19: ">Sắt",
}
k2 = {
    "CD": 0,
    "CN": 1,
    "CL": 2,
    "CS": 3,
    "DN": 4,
    "DL": 5,
    "DS": 6,
    "LN": 7,
    "NS": 8,
    "LS": 9,
}


def countCards(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d1[i] + " " + l[j]]
    for c in deck:
        if c[0] == 0:
            p += [k1[c[1]]]
    print(", ".join(p))


def textCountCards(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d1[i] + " " + l[j]]
    for c in deck:
        if c[0] == 0:
            p += [k1[c[1]]]
    return ", ".join(p)


def textCountCard(deck, type):
    p = []
    for j in range(1, 4):
        if deck.count((type, j)) != 0:
            p += [str(deck.count((type, j))) + " " + d1[i] + " " + l[j]]
    return ", ".join(p)


def textCountSpecialCards(deck, type, length):  # [1] Song chủng [2] Biến chủng
    p = []
    if type == 1:
        for i in range(10):
            if deck.count((0, i)) == 1:
                p += [k1[i]]
    else:
        for i in range(10, 20):
            if deck.count((0, i)) == 1:
                p += [k1[i]]
    p1 = p[:length]
    p2 = p[length:]
    return [", ".join(p1) + [",", ""][len(p2) == 0], ", ".join(p2)]


def drawCard(card):
    if card[0] == 0:
        print(k1[card[1]])
    else:
        print(d1[card[0]] + " " + l[card[1]])


def ACTION():
    global action
    action = int(
        input(
            "[1] Xung trận".ljust(26)
            + "| "
            + "[2] Bố trí mai phục".ljust(24)
            + "| "
            + "[3] Tiến hành phục kích".ljust(24)
            + "|\n"
            + "[4] Kiểm tra các quân khu".ljust(26)
            + "| "
            + "[5] Quân khu bị phá hủy".ljust(24)
            + "| "
            + "[0] Hoãn binh".ljust(24)
            + "| => "
        )
    )
    ENTER()
    checkAction()


def checkAction():
    global action
    while action == 2 and lguard and rguard:
        print("Bạn không thể thêm quân vào các điểm mai phục nữa!")
        ENTER()
        ACTION()

    while action == 3 and not lguard and not rguard:
        print("Bạn chưa có quân ở các điểm mai phục!")
        ENTER()
        ACTION()

    while action == 5 and not territory:
        print("Bạn chưa có quân khu trên lãnh thổ!")
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
    a += [d2[c]]
n = int(input("Số lượng người chơi: "))
m = int(input("Thứ tự lượt chơi của bạn: ")) - 1
while m < 0 or m >= n:
    m = int(input("Vui lòng nhập lại thứ tự lượt chơi của bạn: ")) - 1
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
lguardX = []
rguard = []
rguardX = []
guard = []

while True:
    print(" " + "-" * 99)
    print(
        "|"
        + (
            "Bạn có đội quân "
            + str(
                sum(
                    [
                        sum(j * hand.count((i, j)) for j in range(1, 4))
                        for i in range(1, 6)
                    ]
                )
                + sum(hand.count((0, i)) for i in range(10))
            )
            + " năm kinh nghiệm đang sẵn sàng xung trận"
        ).center(99)
        + "|"
    )
    print("|" + "-" * 99 + "|")
    for i in range(1, 6):
        x = str(sum(j * hand.count((i, j)) for j in range(1, 4)))
        print(
            "|"
            + (x + " " + d1[i]).center(49)
            + "|"
            + textCountCard(hand, i).center(49)
            + "|"
        )
        print("|" + "-" * 99 + "|")
    sc = sum(hand.count((0, i)) for i in range(10))
    if sc <= 5:
        print(
            "|"
            + (str(sc) + " Song chủng").center(49)
            + "|"
            + textCountSpecialCards(hand, 1, 5)[0].center(49)
            + "|"
        )
    else:
        print(
            "|"
            + (str(sc) + " Song chủng").center(49)
            + "|"
            + textCountSpecialCards(hand, 1, 5)[0].center(49)
            + "|"
        )
        print(
            "|".ljust(50) + "|" + textCountSpecialCards(hand, 1, 5)[1].center(49) + "|"
        )
    # print("|" + "-" * 99 + "|")
    # bc = sum(hand.count((0, i)) for i in range(10, 20))
    # if bc <= 5:
    #     print(
    #         "|"
    #         + (str(bc) + " Biến chủng").center(49)
    #         + "|"
    #         + textCountSpecialCards(hand, 2, 5)[0].center(49)
    #         + "|"
    #     )
    # else:
    #     print(
    #         "|"
    #         + (str(bc) + " Biến chủng").center(49)
    #         + "|"
    #         + textCountSpecialCards(hand, 2, 5)[0].center(49)
    #         + "|"
    #     )
    #     print(
    #         "|".ljust(50) + "|" + textCountSpecialCards(hand, 2, 5)[1].center(49) + "|"
    #     )
    print("|" + "-" * 99 + "|")
    print(
        "|"
        + "Điểm mai phục trái".center(24)
        + "|"
        + (["Chưa có", textCountCards(lguard)][len(lguard) != 0]).center(24)
        + "|"
        + "Điểm mai phục phải".center(24)
        + "|"
        + (["Chưa có", textCountCards(rguard)][len(rguard) != 0]).center(24)
        + "|"
    )
    print(" " + "-" * 99 + " ")
    ENTER()

    ACTION()

    if action == 1:
        s = int(
            input(
                "Mục đích xuất quân: [1] Bảo vệ lãnh thổ | [2] Tấn công đối thủ | [3] Đóng quân | => "
            )
        )
        ENTER()
        if s == 1:
            t = input("Chọn quân để bảo vệ lãnh thổ: ").upper()
            ENTER()
        elif s == 2:
            t = input("Chọn quân để tấn công đối thủ: ").upper()
            ENTER()
        else:
            t = input("Chọn quân để đóng quân trên lãnh thổ của đối thủ: ").upper()
            ENTER()
        card = []
        cardChange = []
        for c in t.split():
            if len(c) == 3:
                card += [(d3[c[1]], int(c[2]))] * int(c[0])
            else:
                card += [(0, k2["".join(sorted(c[:2]))])]
                cardChange += [(d3[c[3]], 1)]
        while any([x not in hand for x in card]):
            t = input(
                "Quân bạn đã chọn không sẵn sàng!\nVui lòng chọn lại quân khác: "
            ).upper()
            ENTER()
            card = []
            cardChange = []
            for c in t.split():
                if len(c) == 3:
                    card += [(d3[c[1]], int(c[2]))] * int(c[0])
                else:
                    card += [(0, k2["".join(sorted(c[:2]))])]
                    cardChange += [(d3[c[3]], 1)]
        if lguardX and lguardX[0][0] == d3[t.split()[0][1]]:
            h = int(
                input(
                    "Dùng quân mai phục ở cánh trái đã bị lộ diện tham gia tác chiến: [1] Có | [2] Không | => "
                )
            )
            if h == 1:
                guard += lguardX
                lguardX = []
                lguard = []
            ENTER()
        if rguardX and rguardX[0][0] == d3[t.split()[0][1]]:
            h = int(
                input(
                    "Dùng quân mai phục ở cánh phải đã bị lộ diện tham gia tác chiến: [1] Có | [2] Không | => "
                )
            )
            if h == 1:
                guard += rguardX
                rguardX = []
                rguard = []
            ENTER()
        if s == 1:
            print("Quân bạn đã chọn để bảo vệ lãnh thổ là: ", end="")
            countCards(card + guard)
            ENTER()
            territory += card + cardChange + guard
        elif s == 2:
            print("Quân bạn đã chọn để tấn công đối thủ là: ", end="")
            countCards(card + guard)
            ENTER()
            t = int(input("Kết quả của trận đánh: [1] Thắng | [2] Thua | => "))
            ENTER()
            if t == 1:
                k = int(
                    input("Quân thắng trận: [1] Rút về quân khu | [2] Đóng quân | => ")
                )
                ENTER()
                if k == 1:
                    territory += card + cardChange + guard
        else:
            print(
                "Quân bạn đã chọn để đóng quân trên lãnh thổ của đối thủ là: ", end=""
            )
            countCards(card + guard)
            ENTER()
        for c in card:
            hand.remove(c)
            guard = []

    elif action == 2:
        s = input("Chọn quân vào vị trí mai phục: ").upper()
        ENTER()
        card = []
        for c in s.split():
            if len(c) == 3:
                card += [(d3[c[1]], int(c[2]))] * int(c[0])
            else:
                card += [(0, k2["".join(sorted(c))])]
        while any([x not in hand for x in card]):
            s = input(
                "Quân bạn đã chọn không sẵn sàng!\nVui lòng chọn lại quân khác: "
            ).upper()
            ENTER()
            card = []
            for c in s.split():
                if len(c) == 3:
                    card += [(d3[c[1]], int(c[2]))] * int(c[0])
                else:
                    card += [(0, k2["".join(sorted(c))])]
        for c in card:
            hand.remove(c)
        if lguard:
            print("Quân bạn đã chọn vào điểm mai phục phải là: ", end="")
            rguard = card
        else:
            print("Quân bạn đã chọn vào điểm mai phục trái là: ", end="")
            lguard = card
        countCards(card)
        ENTER()

    elif action == 3:
        if lguard:
            print("Điểm mai phục trái: ", end="")
            countCards(lguard)
        else:
            print("Điểm mai phục trái: Chưa có")
        if rguard:
            print("Điểm mai phục phải: ", end="")
            countCards(rguard)
        else:
            print("Điểm mai phục phải: Chưa có")
        ENTER()
        s = int(
            input(
                "[1] Tiến hành phục kích từ cánh trái | [2] Tiến hành phục kích từ cánh phải | => "
            )
        )
        ENTER()
        while (s == 1 and (not lguard or lguardX)) or (
            s == 2 and (not rguard or rguardX)
        ):
            print(
                "Bạn chưa có quân ở điểm mai phục "
                + ["trái", "phải"][s - 1]
                + " hoặc đã bị lộ diện!"
            )
            ENTER()
            s = int(
                input(
                    "[1] Tiến hành phục kích từ cánh trái | [2] Tiến hành phục kích từ cánh phải | => "
                )
            )
            ENTER()
        if s == 1:
            print("Quân mai phục ở cánh trái là: ", end="")
            countCards(lguard)
            for c in lguard:
                if c[0] == 0:
                    t = input("Xác định chủng loại của quân song chủng: ").upper()
                    ENTER()
                    print(
                        "Quân "
                        + textCountCards(lguard)
                        + " đã được chỉ định thành 1 "
                        + d1[d3[t]]
                        + " I!"
                    )
                    lguard.remove(c)
                    lguard += [(d3[t], 1)]
            t = int(
                input("Tình hình ở quân khu: [1] An toàn | [2] Đã bị chiếm đóng | => ")
            )
            ENTER()
            if t == 1:
                print("Quân mai phục ở cánh trái đã rút về quân khu an toàn!")
                territory += lguard
                lguard = []
            else:
                print("Quân mai phục ở cánh trái đã đã bị lộ diện!")
                lguardX = lguard

        if s == 2:
            print("Quân mai phục ở cánh phải là: ", end="")
            countCards(rguard)
            for c in rguard:
                if c[0] == 0:
                    t = input("Xác định chủng loại của quân song chủng: ").upper()
                    ENTER()
                    print(
                        "Quân "
                        + textCountCards(rguard)
                        + " đã được chỉ định thành 1 "
                        + d1[d3[t]]
                        + " I!"
                    )
                    rguard.remove(c)
                    rguard += [(d3[t], 1)]
            t = int(
                input("Tình hình ở quân khu: [1] An toàn | [2] Đã bị chiếm đóng | => ")
            )
            ENTER()
            if t == 1:
                print("Quân mai phục ở cánh phải đã rút về quân khu an toàn!")
                territory += rguard
                rguard = []
            else:
                print("Quân mai phục ở cánh phải đã đã bị lộ diện!")
                rguardX = rguard
        ENTER()

    elif action == 4:
        print(" " + "-" * 99)
        print(
            "|"
            + (
                "Bạn có đội quân "
                + str(
                    sum(
                        [
                            sum(j * territory.count((i, j)) for j in range(1, 4))
                            for i in range(1, 6)
                        ]
                    )
                )
                + " năm kinh nghiệm đã xung trận để bảo vệ các quân khu"
            ).center(99)
            + "|"
        )
        print("|".ljust(100, "-") + "|")
        y = ""
        for i in range(1, 6):
            x = str(sum(j * territory.count((i, j)) for j in range(1, 4)))
            y += "|" + (x + " " + d1[i]).center(19)
        print(y + "|")
        print(" " + "-" * 99)
        ENTER()

    elif action == 5:
        s = input("Quân khu bị phá hủy là: ").upper()
        print("Quân khu " + d1[d3[s]] + " đã bị phá hủy!")
        territory = [x for x in territory if x[0] != d3[s]]
        ENTER()

    if action not in [4, 5]:
        print(("[BẮT ĐẦU LƯỢT " + str(count) + "]").rjust(101, "-"))
        ENTER()
        print("Viện binh: ", end="")
        drawCard(a[deck])
        ENTER()
        hand += [a[deck]]
        deck += n
        count += 1
        if deck >= 70:
            print("Đã hết quân chi viện!")
