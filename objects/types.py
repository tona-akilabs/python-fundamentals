L = [1, 2, 3]
print(type(L))

L = (1, 2, 3)
print(type(L))

L = {1, 2, 3}
print(type(L))
print(isinstance(L, list))
print(isinstance(L, set))

L = {1: 'one', 2: 'two', 3: 'three'}
print(type(L))

print(isinstance(L, dict))