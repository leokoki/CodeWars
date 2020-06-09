from fractions import Fraction 
def mixed_fraction(s):
    signal=''
    n,d = s.split('/')
    if int(n)*int(d)<0:
      signal='-'
      if int(n)<0:n = int(n)*-1
      if int(d)<0:d = int(d)*-1
    num1,resto = int(n)//int(d),int(n)%int(d)
    if resto != 0:
        if num1==0:
            num1 = ''
            fracao = str(Fraction(int(resto),int(d)))
        else:fracao = ' ' + str(Fraction(int(resto),int(d)))
    else:fracao = ''        
    return print(signal+str(num1)+fracao)
mixed_fraction('42/9')    # '4 2/3'
mixed_fraction('6/3')     #'2'
mixed_fraction('4/6')     #'2/3'
mixed_fraction('0/18891') #'0'
mixed_fraction('-10/7')   #'-1 3/7'
mixed_fraction('-22/-7')  #'3 1/7'
# https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python