###########################
#  BaekJoon 11557번
#  by 김승현                
###########################

# Q. Yangjojang of The Year

for _ in range(int(input())):
    max_ac, max_al = '', 0
    for _ in range(int(input())):
        ac, al = input().split()
        al = int(al)
        if al > max_al:
            max_ac = ac
            max_al = al
    print(max_ac)