def counting_sort(num_list, sorted_list, k, l):
    count_list = [0]*(k+1)
    ten_list = [0]*l
    for i in range(l):
        ten_list[i] = int(num_list[i]) // 10
    for i in range(l):
        count_list[ten_list[i]] += 1
    for i in range(1, k+1):
        count_list[i] += count_list[i-1]
    for i in range(l-1, -1, -1):
        sorted_list[count_list[ten_list[i]]-1] = num_list[i]
        count_list[ten_list[i]] -= 1
    return sorted_list

T = int(input())

for t in range(1, T+1):
    l = int(input())
    num_list = input().split()
    sorted_list = [0]*l
    result = counting_sort(num_list, sorted_list, 5, l)
    ans = " ".join(result)
    print("#%d %s" %(t, ans))