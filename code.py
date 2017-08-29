from __future__ import division
import math

"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings


# 1

def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    L_sub = filter(lambda x:x<10, L)
    return L_sub #Add your code here

#Test
print entries_less_than_ten([2, 13, 4, 66, -5]) == [2, 4, -5]

# 2

def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    count = 0
    for l in L:
        if l < 0:
            count += 1
            
    return count

# TEST
print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3

# 3
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    L1 = list(set(L1))
    L2 = list(set(L2))
    
    L_commom = []
    
    for l1e in L1:
        for l2e in L2:
            if l2e in L_commom:
                pass
            else:
                if l1e == l2e:
                    L_commom.append(l1e)
    return L_commom

#TEST
print common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]

#4
def fibonacci_generator():
    """
    Generate the Fibonacci sequence.

    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).
    """
    a1 = 1
    a2 = 0
    
    while 1:
        yield a1
        a2 = a1 + a2
        yield a2
        a1 = a1 + a2

#TEST
f = fibonacci_generator()
print [f.next() for i in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    f = fibonacci_generator()
    fi = f.next()
    #fl = fi
    while fi < n:
        l = fi
        fi = f.next()
    return l

#TEST
print largest_fibonacci_before(55) == 34

#6
def catalan_generator():
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    cn = 0
    ci = 1

    while 1:
        yield ci
        cn += 1
        ci = ci * 2 * (2*cn-1) / (cn+1)

#TEST
c = catalan_generator()
print [c.next() for i in range(10)] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    
    
#7
### CREATE YOUR OWN FUNCTION. Make sure it has a nice docstring.
# See http://www.pythonforbeginners.com/basics/python-docstrings
# for basic tips on docstrings.
def sigmoid(x):
    """
    Returns the value of sigmoid function, S(x) = 1/(1+e^{-x}) for a given `x`.
    """
    return 1/(1 + math.exp(-x))

#TEST
print sigmoid(-0.0458)
