n, k = map(int, input().split())

d = list(input().split())

for i in range(n, 10000):
    flag = True
    num = list(str(i))
    for j in range(len(num)):
        if num[j] in d:
            flag = False

    if flag:
        print(i)
        break
