T = int(input())

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    change_num = [0] * len(change)
    money = int(input())
    for idx in range(len(change)):
        while money >= change[idx]:
            money -= change[idx]
            change_num[idx] += 1
    change_num = map(str, change_num)
    ans = " ".join(change_num)
    print("#%d" % t)
    print("%s" % ans)