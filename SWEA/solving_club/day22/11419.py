#########################
#  SWEA number 11419
#  by 김승현                
#########################

# Q. Baby-Gin Game


def make_combi(combi, visited, cnt):
    if cnt == 6:
        if combi not in combi_nums:
            combi_nums.append(combi)
        return
    for i in range(6):
        if i not in visited:
            make_combi(combi + [nums[i]], visited + [i], cnt + 1)


def check_run(x):
    return True if x[0] + 1 == x[1] and x[1] + 1 == x[2] else False


def check_triplet(x):
    return True if x.count(x[0]) == 3 else False


for t in range(1, int(input())+1):
    nums = list(map(int, input()[:6]))
    combi_nums = []
    make_combi([], [], 0)
    flag = 1
    for combi in combi_nums:
        arg1 = check_run(combi[0:3]) or check_triplet(combi[0:3])
        arg2 = check_run(combi[3:6]) or check_triplet(combi[3:6])
        if arg1 and arg2:
            print("#%d Baby Gin" %t)
            flag = 0
            break
    if flag:
        print("#%d Lose" %t)
