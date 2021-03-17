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

d = {1: "Sắt", 2: "Cây", 3: "Nước", 4: "Lửa", 5: "Đất"}
l = {1: "I", 2: "II", 3: "III"}

def countCard(deck):
    p = []
    for i in range(1, 6):
        for j in range(1, 4):
            if deck.count((i, j)) != 0:
                p += [str(deck.count((i, j))) + " " + d[i] + " " + l[j]]
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
print("[BÀI CỦA BẠN]" + "-" * 50)
print()
countCard(a[5 * m : 5 * (m + 1)])
print()
print("[BẮT ĐẦU]" + "-" * 38 + "[RÚT BÀI: ENTER]")

deck = 5 * n + m
count = 1

while deck < 60:
    input()
    print("Lần " + str(count) + ":")
    drawOneCard(a[deck])
    deck += n
    count += 1
    if deck >= 60:
        print("Hết quân bài ngũ hành để rút!")
