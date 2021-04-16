#########################
#  SWEA number 1966
#  by 김승현                
#########################

# Q. 숫자를 정렬하자

def selection_sort_recursion(x, idx):
    if idx == N-1:
        return x
    min_num = x[idx]
    min_idx = idx
    for i in range(idx, N):
        if x[i] < min_num:
            min_idx = i
            min_num = x[i]
    x[idx], x[min_idx] = x[min_idx], x[idx]
    return selection_sort_recursion(x, idx+1)


for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sort_list = selection_sort_recursion(num_list, 0)
    print("#%d %s" %(t, ' '.join(map(str, sort_list))))