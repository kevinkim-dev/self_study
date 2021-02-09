def recursion_charge(charge_list, pos, move, max_d):
    if pos <= max_d:
        return move
    elif pos - charge_list[-1] > max_d:
        return 0
    else:
        for i in range(len(charge_list)):
            if pos - charge_list[i] <= max_d:
                move += 1
                break
    return(recursion_charge(charge_list[:i], charge_list[i], move, max_d))

T = int(input())

for t in range(1, T+1):
    max_d, dst, charge_num = map(int, input().split())
    charge_list = list(map(int, input().split()))
    ans = recursion_charge(charge_list, dst, 0, max_d)
    print("#%d %d" % (t, ans))