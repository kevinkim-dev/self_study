#########################
#  SWEA number 5550
#  by 김승현                
#########################

# Q. 나는 개구리로소이다

crock = ['c', 'r', 'o', 'a', 'k']

for t in range(1, int(input())+1):
    sound = input()
    frog = [0]*5
    ans = 0
    for i in range(len(sound)):
        if sound[i] == 'c':
            if frog[4]:
                frog[4] -= 1
            frog[0] += 1
        else:
            x = crock.index(sound[i])
            if not frog[x - 1]:
                ans = -1
                break
            else:
                frog[x - 1] -= 1
                frog[x] += 1
    if ans != -1:
        ans = frog[4]
    if frog[0] or frog[1] or frog[2] or frog[3]:
        ans = -1
    print("#%d %d" %(t, ans))