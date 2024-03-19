def knapsack_greedy(values, weights, max_weight):
    n = len(values)
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    for v, w in items:
        if max_weight >= w:
            max_weight -= w
            total_value += v
        else:
            total_value += max_weight * (v/w)
            break
    return total_value

fin = "BAD.INP"
dic = dict()
with open(fin, 'r') as file:
    first = list(map(int, file.readline().strip().split(' ')))
    n = int(first[0])
    w = int(first[1])
    for line in file.readlines():
        lst = line.strip().split(' ')
        dic[lst[2]] = (lst[0], lst[1])
values = list()
weights = list()
for entry in dic:
    values.append(int(dic[entry][1]))
    weights.append(int(dic[entry][0]))
max_values = knapsack_greedy(values, weights, w)
print(n)
print(w)
print(max_values)
# print(values)
# print(weights)