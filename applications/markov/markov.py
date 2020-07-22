import random
words = ''
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
words_to_follow = {}

for i, word in enumerate(words):
    if i == (len(words) - 1):
        continue
    elif words_to_follow.get(word) != None:
        words_to_follow[word].append(words[i+1])
    else:
        words_to_follow[word] = [words[i+1]]

# TODO: construct 5 random sentences
def start_word(words):
    start_word = random.choice(words)
    while (not start_word[0].isupper()):
        if (start_word[0] == '"') and start_word[1].isupper():
            break
        start_word = random.choice(words)

    return start_word

def is_stop_word(word):
    l = len(word)
    punct = ['.','?','!']
    if word[l-1] in punct:
        return True
    elif (word[l-1] == '"') and (word[l-2] in punct):
        return True

    return False

def gen_sentence(words):
    word = start_word(list(words))
    print(word, end=" ")
    while not is_stop_word(word):
        word = random.choice(words[word])
        print(word, end=" ")
    print() # extra print statement to give terminal new line following final word

print('1: ', end="")
gen_sentence(words_to_follow)
print('\n2: ', end="")
gen_sentence(words_to_follow)
print('\n3: ', end="")
gen_sentence(words_to_follow)
print('\n4: ', end="")
gen_sentence(words_to_follow)
print('\n5: ', end="")
gen_sentence(words_to_follow)

