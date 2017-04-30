#!/usr/bin/python -tt

from nltk.corpus import wordnet as wn

word = input("Please enter the word: ")
print("The word sysnset of " + word + " is " + wn.synsets(word))
