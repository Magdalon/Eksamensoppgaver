# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:21:32 2019

@author: magdalon
"""
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

print("""
Oppgave 3 (8 poeng)
En ny vare blir lansert i et område. Vi antar at funksjonen q gitt ved 

    q(t) = 230 * exp(0.015*t), t \in [0,52]

er en god modell for etterspørselen etter varen per uke, t uker etter lanseringen.       
""")

start = 0
slutt = 52
t = symbols("t")
etterspørsel = 230*exp(0.015*t)

print("""
a) Bruk graftegner til å tegne grafen til q.       
""")
plot(etterspørsel,(t,start,slutt),axis_center = (0,230))


print("""
Enhetsprisen for varen settes lik 50 kroner det første året.
b) Bestem inntekten i uke 40 etter lanseringen.       
""")
pris=50
inntekt = pris *etterspørsel
print("Svar:",inntekt.subs({t:40}),"kr")

print("""
c) Bestem den samlede inntekten de første 52 ukene etter lanseringen.       
""")

svar = integrate(inntekt,(t,start,slutt))

print("Svar:",svar,"kr.")

print("""
Etter at varen har vært i markedet i ett år, vil enhetsprisen p kroner være en funksjon av
den ukentlige etterspørselen x. Vi går ut fra at p er gitt ved

    p(x) = -0.01x+60, x \in [500,200]
    
Grensekostnaden ved produksjon av x enheter er

    K'(x) = 0.02x + 25, x \in [500,200]

d) Hva må enhetsprisen være for at overskuddet skal bli størst mulig?       
""")

s = symbols('x')

grensekostnad = 0.02*x+25
kostnad = integrate(grensekostnad,x)
pris = -0.01*x+60
inntekt = pris*x
overskudd = inntekt - kostnad
plot(overskudd,(x,500,2000),axis_center=(500,0))
maks = solve(diff(overskudd),x)
print("Overskuddet er størst når vi produserer", maks, "enheter")
print("da blir prisen",pris.subs({x:maks [0]}),"kr")
