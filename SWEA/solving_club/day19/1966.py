#########################
#  SWEA number 1966
#  by 김승현                
#########################

# Q. 숫자를 정렬하자

def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    arr = merge_sort(a[:mid])
    brr = merge_sort(a[mid:])
    temp = []
    ai = bi = 0
    while ai < len(arr) and bi < len(brr):
        if arr[ai] > brr[bi]:
            temp.append(brr[bi])
            bi += 1
        else:
            temp.append(arr[ai])
            ai += 1
    if bi == len(brr):
        temp += arr[ai:]
    elif ai == len(arr):
        temp += brr[bi:]
    return temp


for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sort_list = merge_sort(num_list)
    ans = ' '.join(map(str, sort_list))
    print("#%d %s" %(t, ans))