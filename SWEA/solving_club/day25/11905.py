#########################
#  SWEA number 11905
#  by 김승현                
#########################

# Q. 병합 정렬

def merge_sort(a):
    global cnt
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
        cnt += 1
    elif ai == len(arr):
        temp += brr[bi:]
    return temp


for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    sort_list = merge_sort(num_list)
    print("#%d %d %d" %(t, sort_list[N//2], cnt))