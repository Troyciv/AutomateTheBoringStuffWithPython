#!/usr/bin/env python3


def list(word):
    description = ''
    for i in spam[:-1]:
        description = description + i + ', '
    description = description + spam[-1] + ' and ' + word
    return (description)


spam = ['apples', 'bananas', 'tofu', 'cats']
word = 'something else'
print(list(word))
