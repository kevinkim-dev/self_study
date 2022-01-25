###########################
#  BaekJoon 1942번
#  by 김승현                
###########################

# Q. 디지털시계

import sys

input = sys.stdin.readline

for _ in range(3):
    st, et = input().split()
    sh, sm, ss = map(int, st.split(':'))
    eh, em, es = map(int, et.split(':'))
    ans = 0
    while sh != eh or sm != em or ss != es:
        if not (sh + sm + ss)%3:
            ans += 1
        ss += 1
        if ss == 60:
            ss = 0
            sm +=1
            if sm == 60:
                sm = 0
                sh += 1
                if sh == 24:
                    sh = 0
    if not (sh + sm + ss)%3:
        ans += 1
    print(ans)