###########################
#  BaekJoon 16431번
#  by 김승현                
###########################

# Q. 베시와 데이지

b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
j1, j2 = map(int, input().split())

b_x = abs(j1-b1)
b_y = abs(j2-b2)
d_x = abs(j1-d1)
d_y = abs(j2-d2)

b_len = max(b_x, b_y)
d_len = d_x + d_y

if b_len == d_len:
    print('tie')
elif b_len > d_len:
    print('daisy')
else:
    print('bessie')
