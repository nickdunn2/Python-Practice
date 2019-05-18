def staircase(num):
    for i in range(1, num + 1):
        print((num - i) * ' ' + i * '#')


n = int(input("How big would you like your staircase? "))
staircase(n)
