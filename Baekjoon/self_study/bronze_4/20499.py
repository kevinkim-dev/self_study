###########################
#  BaekJoon 20499번
#  by 김승현                
###########################

# Q. Darius님 한타 안 함?

k, d, a = map(int, input().split('/'))

print('hasu') if d == 0 or k+a<d else print('gosu')