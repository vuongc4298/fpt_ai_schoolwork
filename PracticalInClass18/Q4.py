def most_appear(f):
    inp = f.read()
    lst = []

    for w in inp.split():
        if w[0].isupper():
            lst.append(w.lower())
        else:
            lst.append(w)

    dic = dict()
    for word in lst:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    count = 0
    words = []
    for w in dic:
        if dic[w] > count:
            count = dic[w]

    for w in dic:
        if dic[w] == count:
            words.append(w)
    return words, count
    
fname = input("Enter file:")
try:
    fin = open(fname, "r")
except:
    print("File cannot be opened:", fname)
    quit()
    
words, count = most_appear(fin)
    
fout = open("f2.txt", "w")
s = ''
for w in words:
    s += w + ' '
s += str(count)
print(s)
fout.write(s)
fin.close()
fout.close()