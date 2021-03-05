a = [1, 2, 3]
b = '123'

a_iter = iter(a)
b_iter = iter(b)

print(type(a_iter))
print(type(b_iter))

print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))