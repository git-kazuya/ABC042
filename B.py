n, l = map(int, input().split())

s = list()

for _ in range(n):
    s.append(input())

newS = sorted(s)

print(''.join(newS))
