def no_dups(s):
    exists = {}
    words = []

    s = s.split()
    for word in s:
        if word in exists:
            continue
        else:
            exists[word] = word
            words.append(word)

    return ' '.join(words)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))