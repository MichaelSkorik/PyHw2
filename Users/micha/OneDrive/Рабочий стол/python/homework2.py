N = int(input("Введите число N: "))
k = 0
power_of_two = 1

while power_of_two <= N:
    print("2 **",k ,"->", power_of_two)
    k += 1
    power_of_two = 2 ** k