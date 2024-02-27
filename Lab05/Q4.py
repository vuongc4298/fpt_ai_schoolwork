import copy

tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

tuple2 = (10, 20, 30, 40)
a = tuple2[0]
b = tuple2[1]
c = tuple2[2]
d = tuple2[3]

print(a)
print(b)
print(c)
print(d)

tuple3 = (11, 22)
tuple4 = (99, 88)

temp = copy.deepcopy(tuple3)
tuple3 = copy.deepcopy(tuple4)
tuple4 = copy.deepcopy(temp)

print(f"tuple3: {tuple3}")
print(f'tuple4: {tuple4}')