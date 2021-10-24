###########################
#  BaekJoon 2902번
#  by 김승현                
###########################

# Q. KMP는 왜 KMP일까?

name = input()

ans = ''
is_first = True
for s in name:
    if is_first:
        ans += s
        is_first = False
    elif s == '-':
        is_first = True
c
print(ans)