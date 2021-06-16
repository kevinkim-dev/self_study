(¹Ì¿Ï)

def find_num(num):
    yaksu_list = []
    if all_nums[num]:
        return all_nums[num]
    for i in range(2, num**(0.5)+1):
        if num % i == 0:
            yaksu_list.append(i)
            yaksu_list.append(num / i)
    for i in range(len(yaksu_list//2)):
        if not all_nums[num]:
            




for t in range(1, int(input())+1):
    num_list, N = list(map(int, input().split())), int(input())
    nums = list()
    M = 1000001
    all_nums = [0]*M
    for i in range(10):
        if num_list[i]:
            nums.append(i)
    for i in range(M):
        flag = 1
        x = str(i)
        for chr in x:
            if int(chr) not in nums:
                flag = 0
                break
        if flag:
            all_nums[i] = len(x)
    find_num(N)