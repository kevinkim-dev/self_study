# ##########################
#  project_euler number 32
#  by 김승현                
# ##########################

# Q. 1~9 팬디지털 곱셈식을 만들 수 있는 모든 수의 합

pandigital_list = []

for i in range(2, 1000):
    for j in range(2, 10000):
        flag = 1
        num_list = [0]*10
        k = i * j
        i1= i
        j1 = j
        k1 = k
        while k1 > 0:
            if num_list[k1 % 10] == 0 and k1 % 10 != 0:
                num_list[k1 % 10] += 1 
                k1 //= 10
            else:
                flag = 0
                break 
        while i1 > 0 and flag == 1:
            if num_list[i1 % 10] == 0 and i1 % 10 != 0:
                num_list[i1 % 10] += 1
                i1 //= 10
            else:
                flag = 0
                break 
        while j1 > 0 and flag == 1:
            if num_list[j1 % 10] == 0 and j1 % 10 != 0:
                num_list[j1 % 10] += 1
                j1 //= 10
            else:
                flag = 0
                break 
        if flag == 1 and sum(num_list) == 9:
            print("%d * %d = %d 는 pandigidal" % (i, j, k))
            if k not in pandigital_list:
                pandigital_list.append(k)         

print(len(pandigital_list))
print(pandigital_list)
print(sum(pandigital_list))

