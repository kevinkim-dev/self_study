###########################
#  BaekJoon 12790번
#  by 김승현                
###########################

# Q. Mini Fantasy War

for _ in range(int(input())):
    A = list(map(int, input().split()))
    HP, MP, ATK, DEF = A[0]+A[4], A[1]+A[5], A[2]+A[6], A[3]+A[7]
    if HP <= 1:
        HP = 1
    if MP <= 1:
        MP = 1
    if ATK <= 0:
        ATK = 0
    print(HP + 5*MP + 2*ATK + 2*DEF)