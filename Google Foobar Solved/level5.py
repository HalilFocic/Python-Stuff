from math import factorial
from collections import Counter
from fractions import gcd

def brojac_ciklus(c, n):
    cc=factorial(n)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b)
    return cc        

def particije(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in particije(n-i, i):
            yield [i] + p
def solution(w, h, s):    
    grid=0
    # Vraca broj unikatnih putanji
    for cpw in particije(w):
        for cph in particije(h):            
            m=brojac_ciklus(cpw, w)*brojac_ciklus(cph, h)
            grid+=m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
    # Vraca str jer je tako u zadatku,sto ne znam
    return str(grid//(factorial(w)*factorial(h)))







