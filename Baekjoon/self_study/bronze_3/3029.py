###########################
#  BaekJoon 3029번
#  by 김승현                
###########################

# Q. 경고

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time1 = h1*60*60 + m1*60 + s1
time2 = h2*60*60 + m2*60 + s2

if time2 < time1:
    time2 += 24*60*60

ans = time2 - time1

ans_h, ans_m, ans_s = str(ans//3600).zfill(2), str(ans // 60 % 60).zfill(2), str(ans % 60).zfill(2)

print(f'{ans_h}:{ans_m}:{ans_s}')