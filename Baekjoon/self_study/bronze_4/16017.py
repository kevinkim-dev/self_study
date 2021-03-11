###########################
#  BaekJoon 16017번
#  by 김승현                
###########################

# Q. Telemarketer or not?

tel = [8, 9]

num = []
for _ in range(4):
    num.append(int(input()))
if num[1] == num[2] and num[0] in tel and num[3] in tel:
    print('ignore')
else:
    print('answer')
