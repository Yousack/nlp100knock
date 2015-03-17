def char_n_gram(s, n):
    n_gram = []
    for i in range(len(s) - n + 1):
        n_gram.append(s[i:i + n])

    return n_gram


def word_n_gram(s, n):
    n_gram = []
    word_list = s.split(" ")
    for i in range(len(word_list) - n + 1):
        n_gram.append(word_list[i:i + n])

    return n_gram

s = "I am an NLPer"

print(char_n_gram(s, 2))
print(word_n_gram(s, 2))
