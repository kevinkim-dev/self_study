###########################
#  BaekJoon 14935번
#  by 김승현                
###########################

# Q. FA

num = input()

while True:
    new_num = str(int(num[0])*len(num))
    if new_num == num:
        print('FA')
        break
    else:
        num = new_num