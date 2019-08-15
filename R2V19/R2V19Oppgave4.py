# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:21:28 2019

@author: magdalon
"""

from sympy import *
from scipy.integrate import quad

print("""
Oppgave 4 (6 poeng)
En sirkel har sentrum i (0, 5) og radius 2. Vi roterer denne sirkelen 360 \deg om x-aksen.
Da får vi et omdreiingslegeme som vist på figuren. 
""")

print("""
Forklar at grafene til f og g til sammen danner sirkelen når f og  g er gitt ved

f(x) = 5+sqrt(4-x**2)

g(x) = 5-sqrt(4-x**2)

""")

print("Disse skal til sammen gi en hel sirkel:")
print("Løser baklengs")


x = symbols('x')
y = symbols('y')


sirkel = x**2+(y-5)**2
radius = 2
print(Eq(sirkel,radius**2))
løsning = solveset(Eq(sirkel,radius**2),y)

print(y,"=",løsning)

print("""
b) Bruk CAS til å bestemme den eksakte verdien for volumet av omdreiingslegemet. 
""")

ytterside = 5 + sqrt(4-x**2)
innerside = 5 - sqrt(4-x**2)

volum = integrate(pi*(ytterside**2-innerside**2),(x,-2,2))
print("Svar:",volum)
print("Svar:",volum.evalf())

print("""
En annen sirkel har sentrum i (2, 7) og radius 3. Vi roterer også denne sirkelen 360\deg om x-aksen.
c) Bruk CAS til å bestemme den eksakte verdien for volumet av dette
omdreiingslegemet. 
""")
sentrum = Point(2,7)
radius = 3
løsning = solveset((x-sentrum.x)**2+(y-sentrum.y)**2-radius**2,y)
ytterside = løsning.args[0]
innerside = løsning.args[1]
integrand = pi*(ytterside**2-innerside**2)

volum = integrate(integrand,(x,0,1))

#print("Svar:", volum)

# Vi får ikke en god løsning, vi må bruke numerisk integrasjon.
integrand = pi*(ytterside**2-innerside**2)
numeriskIntegrand = lambdify(x,integrand,'numpy')
svar = quad(numeriskIntegrand,sentrum.x-radius,sentrum.x+radius)
volum = svar[0]
print("Numerisk svar:",volum)
