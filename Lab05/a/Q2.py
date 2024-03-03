numbers = [1, 2, 3, 4, 5, 6, 7]
squared = [i**2 for i in numbers]
print(squared)

list1 = ["Hello", "take"]
list2 = ['Dear', 'Sir']

list3 = [list1[i] + ' ' + list2[j] for i in range(0, len(list1)) for j in range(0, len(list2))]
print(list3)