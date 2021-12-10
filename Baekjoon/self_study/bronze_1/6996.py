###########################
#  BaekJoon 6996번
#  by 김승현                
###########################

# Q. 애너그램

def check_ana():
    for k in a_dict.keys():
        if a_dict[k] != b_dict.get(k):
            return False
    return True

for _ in range(int(input())):
    a, b = input().split()
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
        continue
    l = len(a)
    a_dict, b_dict = dict(), dict()
    for i in range(l):
        a_dict[a[i]] = a_dict.get(a[i], 0) + 1
        b_dict[b[i]] = b_dict.get(b[i], 0) + 1
    ana = check_ana()
    if ana:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')

        

