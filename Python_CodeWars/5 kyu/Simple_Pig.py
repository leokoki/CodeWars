'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

import string
def pig_it(text):
    text = text.split()
    s=[]
    for word in text: 
        if not word in string.punctuation: s.append(str(word[1:]) + str(word[0]) + 'ay')
        else: s.append(word)
    return print(' '.join(s))
    #your code here

pig_it('Pig latin is cool !')
#,'igPay atinlay siay oolcay !')
pig_it('This is my string')
# 'hisTay siay ymay tringsay')