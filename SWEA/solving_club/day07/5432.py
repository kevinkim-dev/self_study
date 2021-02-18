#########################
#  SWEA number 5432
#  by 김승현                
#########################

for t in range(1, int(input())+1):
    pos = input()
    cut_count = 0
    cut = 0
    i = 0
    while i < len(pos)-1:
        if pos[i] == '(':
            if pos[i+1] == ')':
                cut_count += cut
                i += 1
            else:
                cut += 1
        else:
            cut_count += 1
            cut -= 1
        i += 1
    cut_count += cut
    print("#%d %d" %(t, cut_count))

