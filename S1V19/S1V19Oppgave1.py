# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:39:54 2019

@author: magdalon
"""

from scipy.optimize import linprog
import scipy as sp
import numpy as np
from sympy import *
print("""
På grunn av streik har bakermester Snipp begrenset tilgang på råvarer. En dag har han til rådighet
* 50 kg mel
* 7 kg sukker
* 8.5 kg smør

Han lager kaker av type A og V. Tabellen nedenfor viser ingrediensene i en kake for hver av de to kaketypene.

Kaketype   Mel   Sukker   Smør
A          300      100    125
B          500       50     50

La x være antall kaker han baker av type A, og y være antall kaker han baker av type B, denne dagen.
""")

print("""
Forklar at x og y må tilfredstille ulikhetene.
x => 0
y => 0
3x + 5y <= 500
2x + y <= 140
5x + 2y <= 340
""")

print("Se løsningsforslag")

print("""
b) Skraver i et koordinatsystem området som er avgrenset av ulikhetene.
""")

A = [[.300,.500],[.100,.050],[.125,.050]]
b = [50,7,8.5]
x = symbols('x')

g0 = (b[0]-A[0][0]*x)/A[0][1]
g1 = (b[1]-A[1][0]*x)/A[1][1]
g2 = (b[2]-A[2][0]*x)/A[2][1]

plot_implicit(y<Min(g0,g1,g2),(x,0,Min(solve(g0)[0],solve(g1)[0],solve(g2)[0])),(y,0,min(g0.subs({x:0}),g1.subs({x:0}),g2.subs({x:0}))),ylabel = "y")

print("""
Bakermester Snipp har en fortjeneste på 160 kroner per kake for kaker av type A og 120 kroner per kake for kaker av type B.

c) Hvor mange kaker av hver type må han bake for at fortjenesten skal bli størst mulig?
   Hva blir fortjenesten da?
""")
c = [-160,-120]

res = linprog(c,A,b)
print(res)

# Vi ser at vi ikke får en diskret løsning. Diskret optimering gjør at vi må løse knapsack-problemet. På grunn av strukturen trenger vi bare å se på to verdier
typeA = sp.floor(res.x[0])
res2 = linprog(c,A,b,bounds=((typeA,typeA),(None,None)))
res3 = linprog(c,A,b,bounds=((typeA+1,typeA+1),(None,None)))
print("---")
if (res2.fun < res3.fun):
    print(res2)
else:
    print(res3)
print("""
En dag er en av ovnene han bruker til å steke kaker av type B i, i ustand. Dette gjør at han høyst kan lage 70 kaker av type B denne dagen.

d) Hvor mange kaker av hver type må han bake denne dagen for at fortjenesten skal bli størst mulig?
""")
maxB = 70
resD = linprog(c,A,b,bounds=((None,None),(None,maxB)))
print(resD)