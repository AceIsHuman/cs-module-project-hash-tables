def word_count(s):
    word_count = {}
    char_to_ignore = ['"',':',';',',','.','-','+','=','/',"\\",'|','[',']','{','}','(',')','*','^','&']

    words = s.split()
    for word in words:
        word = word.lower()
        if not word.isalpha():
            ignored_char = ''
            for char in word:
                if char not in char_to_ignore:
                    ignored_char = ignored_char + char
            word = ignored_char
        if word in word_count:
            word_count[word] = word_count[word] + 1
        elif word != '': word_count[word] = 1

    return word_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))