###########################
#  BaekJoon 10768번
#  by 김승현                
###########################

# Q. 특별한 날

month = int(input())
day = int(input())

if month > 2 or (month == 2 and day > 18):
    print('After')
elif month == 1 or (month == 2 and day < 18):
    print('Before')
else:
    print('Special')