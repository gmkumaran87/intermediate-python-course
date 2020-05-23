n = int(input())

b = bin(n)
c = 0
cnt = []
for num in b[2:]:
    if num == '1':
        c += 1
    else:
        cnt.append(c)
        c = 0
cnt.append(c)
max_1 = max(cnt)

print(cnt, max_1)
