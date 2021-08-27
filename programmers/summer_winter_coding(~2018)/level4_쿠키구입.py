def solution(cookie):
    l = len(cookie)
    cl_list, cr_list = [[] for _ in range(l)], [[] for _ in range(l)]   
    for i in range(l):
        cl_list[i].append(cookie[i])
        cr_list[i].append(cookie[i])
    for i in range(1, l):
        for j in range(i):
            cl_list[i-1][j]
        left_cookie = list(map(lambda x: x+cl_list[i][0], cl_list[i-1]))
        right_cookie = list(map(lambda x: x+cr_list[l-i-1][0], cr_list[l-i]))
        cl_list[i].extend(left_cookie)
        cr_list[l-i-1].extend(right_cookie)
    answer = 0
    for i in range(l-1):
        cl, cr = cl_list[i], cr_list[i+1]
        for c in cl:
            if c in cr:
                answer = max(answer, c)
    
    return answer