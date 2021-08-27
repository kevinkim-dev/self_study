def solution(dice):
    def check_make():
        for key in num_dict.keys():
            if num_dict.get(key, 0) > nums.get(key, 0):
                return False
        return True
    
    nums = dict()
    for di in dice:
        d_v = [0]*10
        for d in di:
            if not d_v[d]:
                nums[d] = nums.get(d, 0) + 1
                d_v[d] = 1
    for i in range(1, 10000):
        num = str(i)
        num_dict = dict()
        for n in num:
            num_dict[int(n)] = num_dict.get(int(n), 0) + 1
        if not check_make():
            return int(num)

dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
print(solution(dice))