def is_anagram(word1, word2):
    k = 0
    a1 = sorted(word1)
    a2 = sorted(word2)

    for i in a1:
        if i == " ":
            k += 1
    del a1[:k]
    k = 0

    for i in a2:
        if i == " ":
            k += 1
    del a2[:k]
    k = 0

    print(a2)

    if a1 == a2:
        return "Anagram"
    else:
        return "Non anagram"


a = "анаграмма"
b = "мама ранг а"
print(is_anagram(a, b))
