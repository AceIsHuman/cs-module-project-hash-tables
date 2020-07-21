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
# Your code here

