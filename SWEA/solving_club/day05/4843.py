#########################
#  SWEA number 4843
#  by 김승현                
#########################

# Q. 특별한 정렬

def special_sort(num_list, i):
    if i == len(num_list):
        return
    if i % 2 == 0:
        max_index = i
        for n in range(i, len(num_list)):
            if num_list[n] >= num_list[max_index]:
                max_index = n
        num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
    else:
        min_index = i
        for n in range(i, len(num_list)):
            if num_list[n] <= num_list[min_index]:
                min_index = n
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return special_sort(num_list, i+1)

for t in range(1, int(input())+1):
    length = int(input())
    num_list = list(map(int, input().split()))
    special_sort(num_list, 0)
    print("#%d" %t, end=' ')
    print(*num_list[:10])