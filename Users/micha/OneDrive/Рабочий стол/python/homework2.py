import math

S = int(input())
P = int(input())
D = S ** 2 - P * 4

if D < 0:
    print("Нет целых корней. Петя допустил ошибку в подсказках.")
else:
    Y1 = (S + math.sqrt(D)) / 2
    Y2 = (S - math.sqrt(D)) / 2

    X1 = S - Y1
    X2 = S - Y2

    if X1.is_integer() and Y1.is_integer() and X1 > 0 and Y1 > 0:
        print(f"Возможные числа X и Y: {int(X1)}, {int(Y1)}")
    if X2.is_integer() and Y2.is_integer() and X2 > 0 and Y2 > 0:
        print(f"Возможные числа X и Y: {int(X2)}, {int(Y2)}")




