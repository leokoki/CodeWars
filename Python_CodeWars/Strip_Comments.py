"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
## https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(txt,markers):
    #your code here
    resultado=[]
    for row in txt.split('\n'):
        for m in markers:
            if m in row:
                row = row.split(m)[0].strip()
            if m == markers[len(markers)-1]:
                resultado.append(row)
    if resultado==[]:
        return print(txt)
    else:
        return print('\n'.join(resultado))

t=25
b=3*t
print('*'*t+'1 exemplo'+'*'*t) 
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])    
# #"apples, pears\ngrapes\nbananas")
print('-'*b)
print('*'*t+'2 exemplo'+'*'*t)
solution("a #b\nc\nd $e f g", ["#", "$"])                                       
# #"a\nc\nd")
print('-'*b)
print('*'*t+'3 exemplo'+'*'*t)
solution('oranges avocados lemons apples\nlemons oranges avocados\napples\npears strawberries\nstrawberries watermelons oranges ! ^', [])
# #'oranges avocados lemons apples\nlemons oranges avocados\napples\npears strawberries\nstrawberries watermelons oranges ! ^'
print('-'*b)
print('*'*t+'4 exemplo'+'*'*t)
solution("bananas bananas strawberries oranges avocados\navocados ' bananas bananas strawberries @\ncherries pears oranges ! apples -\n? =\nstrawberries , ? cherries", ['=', '#', "'", '.', '?', ',', '@'])
#'bananas bananas strawberries oranges avocados\navocados\ncherries pears oranges ! apples -\n\nstrawberries'
