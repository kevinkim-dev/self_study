#########################
#  SWEA number 1221
#  by 김승현                
#########################

# Q. GNS

for t in range(1, int(input())+1):
    case_num, length = map(str, input().split())
    length = int(length)
    num_list = list(map(str, input().split()))
    sort_list = [0]*length
    num_dict = {"ZRO" : 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    num_count = [0]*10
    for num in num_list:
        num_count[num_dict[num]] += 1
    for i in range(9):
        num_count[i+1] += num_count[i]   
    for num in num_list:
        sort_list[num_count[num_dict[num]]-1] = num
        num_count[num_dict[num]] -= 1
    ans = " ".join(sort_list)
    print(case_num)
    print(ans)
