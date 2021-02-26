#########################
#  SWEA number 5789
#  by 김승현  
#########################

# Q. 현주의 상자바꾸기

T = int(input())

for t in range(1, T+1):
    box_num, work_num = map(int, input().split())
    box_list = [0]*box_num
    for work in range(1, work_num+1):
        L, R = map(int, input().split())
        for workspace in range(L-1, R):
            box_list[workspace] = work

    for i in range(len(box_list)):
        box_list[i] = str(box_list[i])
    ans = " ".join(box_list)
    print("#%d %s" % (t, ans))