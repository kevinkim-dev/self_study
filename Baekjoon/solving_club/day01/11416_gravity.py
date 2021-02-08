T = int(input())

for t in range(1, T+1):
    row = int(input())
    box_list = list(map(int, input().split()))
    max_height = 0
    for i in range(len(box_list)):
        cnt = 0
        for j in range(i+1, len(box_list)):
            if box_list[i] <= box_list[j]:
                continue
            cnt += 1
        if cnt > max_height:
            max_height = cnt
    print("#%d %d" % (t, max_height))
