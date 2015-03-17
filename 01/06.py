def char_n_gram(s, n):
    n_gram = []
    for i in range(len(s) - n + 1):
        n_gram.append(s[i:i + n])

    return n_gram

X = set(char_n_gram("paraparaparadise", 2))
Y = set(char_n_gram("paragraph", 2))

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

if 'se' in X:
    print("X includes 'se'")

if 'se' in Y:
    print("Y includes 'se'")
