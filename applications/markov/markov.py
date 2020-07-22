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
