def knapsack_greedy(values, weights, max_weight):
    cnt = dict()
    items = sorted(zip(values, weights), key=lambda x: (x[0]/x[1], x[0]), reverse=True)
    # print(items)
    total_value = 0
    for v, w in items:
        while max_weight >= w:
            max_weight -= w
            total_value += v
            if (v, w) not in cnt:
                cnt[(v, w)] = 1
            else:
                cnt[(v, w)] += 1
    return total_value, cnt

fin = "BAD.INP"
values = list()
weights = list()
with open(fin, 'r') as file:
    first = list(map(int, file.readline().strip().split(' ')))
    n = int(first[0])
    w = int(first[1])
    for line in file.readlines():
        lst = line.strip().split(' ')
        values.append(int(lst[0]))
        weights.append(int(lst[1]))

max_values, cnt = knapsack_greedy(values, weights, w)
print(max_values)
for item in cnt:
    print(f"{item}: {cnt[item]}")