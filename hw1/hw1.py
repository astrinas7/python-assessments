from operator import *
from math import sqrt

#>>>>>>>>>>>>>>>>>>>>> Askhsh 1 <<<<<<<<<<<<<<<

def magnitude(x1, x2):
    """ Ypologizei to mikos dianysmatos (x1, x2).

    x1, x2 -- ari8moi

    Ypologizei tin tetragwniki riza tou x1**2 + x2**2.
    >>> magnitude(0, 0)
    0.0
    >>> magnitude(0, -1) == 1.0
    True
    >>> round(magnitude(1, 1), 10)
    1.4142135624
    """
    """ Xrhsimopoihste MONO klhtikes ekfraseis,
        p.x., stis add, mul, pow, sqrt, ...
        OXI infix telestes (+,-,...) """

    return sqrt(add(pow(x1,2),pow(x2,2)))



#>>>>>>>>>>>>>>>>>>>>> Askhsh 2 <<<<<<<<<<<<<<<

def my_max(x, y):
    """ Ypologizei tin megisti timi

    x,y -- ari8moi

    >>> my_max(2, 45)
    45
    >>> my_max(-894, 2.3)
    2.3
    >>> my_max(9, -20) == 9
    True
    """

    """ Xrhsimopoihste MONO klhtikes ekfraseis (ektos max),
        OXI infix telestes (+,-,...) """

    return x if gt(x,y) else y


#>>>>>>>>>>>>>>>>>>>>> Askhsh 3 <<<<<<<<<<<<<<<

def func0(s):
    """Symplhrwste ta kena wste na didetai to
       akolou8o apotelesma

    >>> func0('I') + ' ' + func0('Bi') + ' ' + 'Spider'
    'Itsy Bitsy Spider'
    """

    return s + "tsy"



#>>>>>>>>>>>>>>>>>>>>> Askhsh 4 <<<<<<<<<<<<<<<

def func1(n, c, s):
    """Symplhrwste ta kena wste:

    >>> func1(1, '*', '-')
    '*'
    >>> func1(2, '*', '-')
    '**-**'
    >>> func1(3, '*', '-')
    '***-***-***'
    >>> func1(4, 'z', 'Z')
    'zzzzZzzzzZzzzzZzzzz'
    >>> func1(1, '-', '*') == '-'
    True
    """
    return n*c if n==1 else (c*n+s)*(n-1)+(c*n)



#>>>>>>>>>>>>>>>>>>>>> Askhsh 5 <<<<<<<<<<<<<<<

def greet(name):
    """Symplhrwste ta kena wste na didetai to
       akolou8o apotelesma

    >>> greet('Mary')
    Hello Mary
    >>> greet('John')
    Hello John
    >>> print(greet('None'))
    Hello None
    None
    """
    print ("Hello " + name)



#>>>>>>>>>>>>>>>>>>>>> Askhsh 6 <<<<<<<<<<<<<<<

def func2(s):
    """Symplhrwste ta kena wste na didetai to
       akolou8o apotelesma

    >>> func2('la')
    'la-la'
    >>> func2(func2('la'))
    'la-la-la-la'
    >>> func2(func2(func2('la')))
    'la-la-la-la-la-la-la-la'
    """

    return s + "-" + s

    


#>>>>>>>>>>>>>>>>>>>>> Askhsh 7 <<<<<<<<<<<<<<<

def digit_sum(x):
    """Ypologizei to a8roisma twn (dekadikwn) pshfiwn tou x

    x -- 8etikos akeraios

    >>> digit_sum(10000)
    1
    >>> digit_sum(615)
    12
    >>> digit_sum(23) == 5
    True
    """
    s = 0
    while x>0:
        s = s + (x%10)
        x = x//10

    return s


#>>>>>>>>>>>>>>>>>>>>> Askhsh 8 <<<<<<<<<<<<<<<

def keep_summing(x):
    """Ypologizei to a8roisma twn pshfiwn synexws ews
    otou to apotelesma exei ena mono pshfio

    x -- 8etikos akeraios

    >>> keep_summing(3)
    3
    >>> keep_summing(32)
    5
    >>> keep_summing(344)
    2
    >>> keep_summing(999)
    9
    >>> print(keep_summing(999))
    9
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
     

    s = 0
     
    while x > 0 :
     	s = s + x % 10
     	x = x//10
     	z = s + x

    if z>10 :
     		 z = (s + x)%10 + (s + x)//10

    return z
     

#>>>>>>>>>>>>>>>>>>>>> Askhsh 9 <<<<<<<<<<<<<<<

def draw_number(x):
    """Emfanizei ton xarakthra + 'h - x fores

    >>> draw_number(5)
    +++++
    >>> draw_number(0)
    >>> draw_number(-3)
    ---
    >>> draw_number(2) == None
    ++
    True
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    return "+"*x if x>0 else "-"* abs(x)
    print("+"*x if x>0 else "-"* abs(x))


#>>>>>>>>>>>>>>>>>>>>> Askhsh 10 <<<<<<<<<<<<<<<

def min_digit(x):
    """Ypologizei to mikrotero pshfio tou x

    x -- 8etikos akeraios

    >>> min_digit(45874543)
    3
    >>> min_digit(98287334) - min_digit(8)
    -6
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    return min(map(int,str(x)))


#>>>>>>>>>>>>>>>>>>>>> Askhsh 11 <<<<<<<<<<<<<<<

def count_digit(x, i):
    """Ypologizei to plh8os twn emfanisewn enos pshfiou

    x -- 8etikos akeraios
    i -- pshfio (1 = 1o pshfio apo dexia, 2 = 2o apo dexia, ktl.)

    >>> count_digit(1000, 1)
    3
    >>> count_digit(12944342, 2)
    3
    >>> count_digit(121,1) == 2
    True
    """
    """ GRAPSTE TON KWDIKA SAS APO KATW """
    
    digit = ( x % (10**i)) // 10**(i-1)

    c=0

    while x > 0:
   
      if (x % 10) == digit :
   	   c = c + 1

      x = x // 10

    return c
