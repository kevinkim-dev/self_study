###########################
#  BaekJoon 5543번
#  by 김승현                
###########################

# Q. 상근날드

min_ham = 2000
min_bev = 2000

for i in range(3):
    ham = int(input())
    if ham < min_ham:
        min_ham = ham
for j in range(2):
    bev = int(input())
    if bev < min_bev:
        min_bev = bev
print(min_ham + min_bev -50)