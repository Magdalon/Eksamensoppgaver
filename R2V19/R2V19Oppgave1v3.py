# -*- coding: utf-8 -*-

# laster inn nødvendige biblioteker
from sympy import *
import numpy as np #sin, diff, linspace, pi
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print("""
Oppgave 1 (6 poeng)

Tabellen nedenfor viser vannstanden til tidevannet ved Leirvik på Stord 14. august 2018.
Vannstanden er målt fra et nullnivå som heter sjøkartnull.

Klokkeslett    03.00  06.00  09.00  12.00  15.00  18.00  21.00  23.00
Vannstand (cm)   102     26     10     81    109     43     20     57
""")

print("a) Bruk tallene fra tabellen til å lage en sinusfunksjon g som er en god modell for vannstanden.")
# laster inn dataene
klokkeslett = [03.00,  06.00,  09.00,  12.00,  15.00,  18.00,  21.00,  23.00]
vannstand = [102, 26, 10, 81, 109, 43, 20, 57]

# lager en mal for sinusfunksjoner, siden skal funksjonen optimize finne verdiene på a, b, c og d
def sinusfunksjon(x,amplitude,k,c,likevektslinje):
    return amplitude*np.sin(k*x + c) + likevektslinje

# må finne en gjetning for a, b, c og d for å starte optimeringsprosedyren
amplitudeGjett = (max(vannstand)-min(vannstand))/2  # amplituden er lett å regne ut
likevektslinjeGjett = (max(vannstand)+min(vannstand))/2  # likevektslinjen er lett å regne ut

# litt vanskeligere å finne b og c
# k / 2pi = avstand mellom to punkter på grafen i samme fase...
# k / pi  = avstand mellom toppunkt og bunnpunkt.

# bruker at f'(x) er tilnærmet lik a*k når vi er på likevektslinjen. Da er den deriverte størst.
# deriverer numerisk
numeriskDerivert = np.diff(vannstand)/np.diff(klokkeslett)
# finner den største verdien av den deriverte og  deler på a for å finne k
kGjett = max(abs(numeriskDerivert))/amplitudeGjett

# -c/k er det punktet hvor grafen krysser likevektslinjen for første gang. Setter dette til null
cGjett = 0
print("Finner den beste sinusfunksjonen numerisk")
print("Startverdier for iterasjon:")
print("amplitude:",amplitudeGjett)
print("k:",kGjett)
print("c:",cGjett)
print("likevektslinje:",likevektslinjeGjett)
print()

parametre, kovarianser = curve_fit(sinusfunksjon,klokkeslett, vannstand, p0=[amplitudeGjett, kGjett, cGjett, likevektslinjeGjett])

amplitude, k, c, likevektslinje = parametre
print("Sluttverdier for iterasjon:")
print("amplitude:",amplitude)
print("k:",k)
print("c:",c)
print("likevektslinje:",likevektslinje)

vannstandFunksjon=lambda x: sinusfunksjon(x,amplitude,k,c,likevektslinje)

plt.plot(klokkeslett,vannstand,"p")
xVerdier = np.linspace(0,24)
yVerdier = vannstandFunksjon(xVerdier)
plt.plot(xVerdier,yVerdier)
plt.show()

print("Funksjonsuttrykk:", amplitude, "*sin(",k,"*x+",c,") +",likevektslinje)

print("""Funksjonen f gitt ved
f(x) = 130 sin(0,501x- 0,532) + 148
er en god modell for vannstanden til tidevannet i Tromsø x timer etter midnatt
14. august 2018.
""")

print("""Funksjonen f gitt ved
f(x) = 130 sin(0,501x- 0,532) + 148
er en god modell for vannstanden til tidevannet i Tromsø x timer etter midnatt
14. august 2018.
""")

print("b) Bestem perioden til f. Gi en praktisk tolkning av svaret")
a = 130
k = 0.501
c = -0.532
d = 148
periodeTromsø = (2*np.pi/k)

print("Perioden er {0:2.2f}. Det betyr at det er høyvann (og lavvann) hver {0:2.2f} time".format(periodeTromsø))
print()

print("c) Gi en praktisk tolkning av tallene 148 og 130 i modellen f.")
print("148 er likevektslinjen. Det er midt mellom høyvann og lavvann. Likevektslinjen ligger ganske mye over sjøkartnull.")
print("130 er amplituden. Det er avstanden mellom likevektslinjen og høyvann.")
print()

print("d) Ved hvilke tidspunkter øker vannstanden med 50 cm per time?")
x=symbols('x')
expr = a*sin(k*x+c)+d
derivert = diff(expr,x)
løsninger = solveset(Eq(derivert,50),x)
dom = Interval(0,24)
svar = dom.intersect(løsninger).evalf()

def klokkeslett(tid,start = 0):
    timer = int(tid//1)
    minutter = int(round(60*(tid % 1),0))

    if (minutter == 60):
        timer += 1
        minutter = 00

    return "{:02d}.{:02d}".format(timer, minutter)

print("Ved klokkeslettene: ",", ".join(list(map(klokkeslett,list(svar)))))
