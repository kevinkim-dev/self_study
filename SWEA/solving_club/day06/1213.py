#########################
#  SWEA number 1213
#  by 김승현                
#########################

# Q. string

for _ in range(10):
    test_num = int(input())
    m_str = input()
    n_str = input()
    cnt = 0
    for i in range(len(n_str)-len(m_str)+1):
        if n_str[i:i+len(m_str)] == m_str:
            cnt += 1
    print("#%d %d" %(test_num, cnt))