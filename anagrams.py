def anagrams(word, words):
    word = ''.join(sorted(word))
    copy = [i for i in words]
    lst = [''.join(sorted(i)) for i in words]
    same = [copy[i] for i, item in enumerate(lst) if item == word]
    return same

