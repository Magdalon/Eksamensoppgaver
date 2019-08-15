# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:20:45 2019

@author: magdalon
"""

from sympy import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from scipy.optimize import curve_fit

print("""
Oppgave 2 (8 poeng)

En bedrift produserer luer. Bedriften har kartlagt den årlige etterspørselen i en by med 20000 innbyggere, det vil si hvor mange luer de kan få solgt per år i denne byen. Etterspørselen avhenger av prisen. Tabellen nedenfor viser resultatet av kartleggingen.

Pris per lue (x kroner)         100  150  200  250  300
Årlig etterspørsel (Q enheter)  850  660  490  370  280
""")

pris = [100,150,200,250,300]
etterspørsel = [850,660,490,370,280]

def eksponentialfunksjon(x,a,k):
    return a*k**x

parametre,variater = curve_fit(eksponentialfunksjon,pris,etterspørsel)

a,k = parametre

print("Svar: f(x) = ",a,"*",k,"**x")
print("""
a) Bruk regresjon til å bestemme den funksjonen av typen Q(x) = a*b**x som passer best med tallene i tabellen
""")



print("""
I resten av oppgaven går vi ut fra at E gitt ved

    E(x) = 1500*0.995**x
    
er en god modell for den årlige etterspørselsen når prisen x er mellom 50 og 500 kroner.

b) Bruk graftegner til å tegne grafen til E for 50 <= x <= 500.
""")

x = symbols("x")
y = symbols("y")
E = 1500*0.995**x

salg = lambdify(x,E)

xrange = np.linspace(50,500,1000)
yrange = salg(xrange)

plt.plot(xrange,yrange)
plt.show()

print("""
c) Hva må prisen per lue være dersom bedriften skal kunne regne med å selge mer enn 1000 luer per år i denne byen?
""")
plt.plot(xrange,yrange)
plt.plot([50,500],[1000,1000],'r')
plt.show()
eqn = ln(1.5) + ln(0.995)*x
svar = solve(eqn,x)
print("Svar:", svar)
print("""
Bedriften har et ønske om å selge luer for til sammen 100 000 kroner i løpet av et år.

d) Hvilken pris bør de da sette for en lue?
""")
inntekt = lambda x: x*1500*0.995**x
yrange = inntekt(xrange)
plt.plot(xrange,yrange)
plt.plot([50,500],[100000,100000],'r')
plt.show()

print('Grafisk "bevis" for at det bare er to løsninger')
eqn = lambda x: inntekt(x)-100000
s1 = newton(eqn,50)
s2 = newton(eqn,500)

print("Svar:",s1,"eller",s2,"kroner")
