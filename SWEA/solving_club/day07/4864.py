#########################
#  SWEA number 4864
#  by 김승현                
#########################

for t in range(1, int(input())+1):
    m_str = input()
    n_str = input()
    flag = 0
    for i in range(len(n_str)-len(m_str)+1):
        if n_str[i:i+len(m_str)] == m_str:
            print("#%d 1" %t)
            flag = 1
    if flag == 0:
        print("#%d 0" %t)
