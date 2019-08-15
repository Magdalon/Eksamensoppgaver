# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 01:00:39 2019

@author: magdalon
"""

from sympy import *

print("""
Oppgave 1 (6 poeng)

En fotballspiller tok et frispark. Han sparket ballen i retning av motstandernes mål. Ballens posisjon t sekunder etter at frisparket ble tatt, er gitt ved vektorfunksjonen

r(t) = [28*t-3*t**2, 10*t-5*t**2]

Enheten langs aksene er meter.
""")

print("""
a) Bestem banerfarten som ballen fikk da den ble sparket.
""")
t = symbols("t")
r = Matrix([28*t-3*t**2,10*t-5*t**2])
dr = diff(r)
v = sqrt((transpose(dr)*dr)[0])
v0 = v.subs({t:0}).evalf()
print("Svar:",v0)

print("""
b) Hvor lang tid tok det fra ballen ble sparket, til den traff bakken?
""")

svar = solveset(r[1],t).intersect(Interval(0,oo,true,false))
if (len(svar) >0):
    print("Ballen treffer bakken etter:", svar,"sekunder")
else:
    print("Ballen treffer aldri bakken!")

print("""
c) Bestem ballens banefart da den var på sitt høyeste punkt
""")

# høyeste punkt
svar = solveset(diff(r[1])).intersect(Interval(0,oo,true,false))
tid = list(svar)
if len(svar) > 0:
    høyde = r[1].subs({t:list(svar)[0]})
    print("Ballen er på sitt høyeste etter",tid,"sekunder. Da er ballen",høyde,"meter over bakken")
else:
    print("Høyden har ikke noe lokalt maksimum")