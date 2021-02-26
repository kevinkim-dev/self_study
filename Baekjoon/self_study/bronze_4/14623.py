###########################
#  BaekJoon 14623번
#  by 김승현                
###########################

# Q. 감정이입

a = input()
b = input()
a_de = 0
b_de = 0
for bi in range(len(a)):
    a_de += int(a[bi])* (2 ** (len(a)-bi-1))
for bi in range(len(b)):
    b_de += int(b[bi])* (2 ** (len(b)-bi-1))
print(format(a_de*b_de, 'b'))
