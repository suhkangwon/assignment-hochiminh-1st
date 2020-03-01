a = ['문자열', 1, 2, 3, True]
b = ("tuple", 4, 5, 6, False)

print(a[1])

for k in range(0, 5, 1):
    print(b[k])


i = 0
while(i <= 4):
    print(b[i])
    i += 1


def j(tuple):
    for h in tuple:
        print(h)


j(b)
