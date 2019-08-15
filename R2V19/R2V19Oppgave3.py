# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:24:31 2019

@author: magdalon
"""

# importerer bibiloteker
from sympy import *

print("""
Oppgave 3 (5 poeng)

Funksjonen f er gitt ved

f(x) = 1/x**2   
""")

print("""
b) Bruk resultatet fra oppgave a) til å begrunne at S < 2 . 
""")

x = symbols('x')

integralsum =  1+integrate(1/x**2,(x,1,oo))

print("Svar: S<",integralsum)

print("""
c) Bruk CAS til å bestemme en eksakt verdi for S.
""")

k = symbols("k")
rekkesum = Sum(1/k**2,(k,1,oo)).doit()
print("Svar:",rekkesum)