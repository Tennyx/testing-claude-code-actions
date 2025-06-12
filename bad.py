import math
import random

DATA = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def calc(x, y=10, z=[]):
    total = 0
    for i in range(len(x)):
        if x[i] > 0:
            total += math.sqrt(x[i]) * y
            if len(z) > 0:
                for item in z:
                    total += item
            else:
                pass
        elif x[i] == 0:
            total += 0
        else:
            total -= x[i]
    return total

def calc2(a, b, c):
    res = 0
    for i in range(a):
        for j in range(b):
            res += i * j * c
    return res

def printit(res):
    print("Result is: " + str(res))

def get_random_choice():
    choices = ["apple", "banana", "orange", "grape"]
    return random.choice(choices)

def bad_loop():
    i = 0
    while i < 10:
        if i == 5:
            print("Midway")
            break
        elif i == 7:
            print("Almost done")
            # continue
        print(i)
        i += 1

def buggy_func(a, b, c={}):
    c[a] = b
    return c

def main():
    res1 = calc(DATA)
    res2 = calc(DATA, 5)
    res3 = calc(DATA, 2, [1,2,3])
    printit(res1)
    printit(res2)
    printit(res3)

    res4 = calc2(10, 5, 3)
    printit(res4)

    for _ in range(3):
        print(get_random_choice())

    bad_loop()

    d = {}
    d = buggy_func("key1", 100, d)
    d = buggy_func("key2", 200, d)
    print(d)

    x = [1, 2, 3, 4, 5]
    y = []
    for i in range(len(x)):
        y.append(x[i] * 2)
    print("Doubled:", y)

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i == j == k:
                    print("All equal:", i, j, k)
                else:
                    for m in range(2):
                        print("Nested loop", i, j, k, m)

    global DATA
    DATA.append(121)
    print("Updated DATA:", DATA)

    a=10
    b =20
    c =30
    print(a +b +c)

if __name__ == "__main__":
    main()
