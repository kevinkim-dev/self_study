for t in range(1, 11):
    length = int(input())
    building_list = list(map(int, input().split()))
    cnt = 0
    beside = [-2, -1, 1, 2]
    for i in range(2, length-2):
        min_view = 255
        for n in beside:
            if building_list[i] - building_list[i+n] < 0:
                min_view = 0
                break
            elif building_list[i] - building_list[i+n] < min_view:
                min_view = building_list[i] - building_list[i+n]
        cnt += min_view
    print("#%d %d" % (t, cnt))

