s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
head = [0, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2]

genso_table = dict()
i = 1
for w in s.split(" "):
    print(i)
    genso_table[w[0:head[i]]] = i
    i = i + 1

print(genso_table)
