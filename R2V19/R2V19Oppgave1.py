# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:37:17 2019

@author: magdalon

Program som løser oppgave 1, del 2 fra eksamen i Matematikk R2 Vår 2019
"""

# laster inn nødvendige biblioteker
from numpy import array, arccos, sin, diff, linspace, pi
from scipy.optimize import curve_fit, fsolve
from scipy.misc import derivative
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

print("Tegner dataene")
plt.plot(klokkeslett,vannstand,"p")
plt.show()

# lager en mal for sinusfunksjoner, siden skal funksjonen optimize finne verdiene på a, b, c og d
def sinusfunksjon(x,amplitude,k,c,likevektslinje):
    return amplitude*sin(k*x + c) + likevektslinje

# må finne en gjetning for a, b, c og d for å starte optimeringsprosedyren
amplitudeGjett = (max(vannstand)-min(vannstand))/2  # amplituden er lett å regne ut
likevektslinjeGjett = (max(vannstand)+min(vannstand))/2  # likevektslinjen er lett å regne ut

# litt vanskeligere å finne b og c
# k / 2pi = avstand mellom to punkter på grafen i samme fase...
# k / pi  = avstand mellom toppunkt og bunnpunkt.

# bruker at f'(x) er tilnærmet lik a*k når vi er på likevektslinjen. Da er den deriverte størst.
# deriverer numerisk
numeriskDerivert = diff(vannstand)/diff(klokkeslett)
# finner den største verdien av den deriverte og  deler på a for å finne k
kGjett = max(abs(numeriskDerivert))/amplitudeGjett

# -c/k er det punktet hvor grafen krysser likevektslinjen for første gang. Setter dette til null
cGjett = 0

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
x = linspace(0,24)
y = vannstandFunksjon(x)
plt.plot(x,y) 
plt.show()

print("Funksjon", amplitude, "*sin(",k,"*x+",c,") +",likevektslinje)

print("""Funksjonen f gitt ved
f(x) = 130 sin(0,501x- 0,532) + 148 
er en god modell for vannstanden til tidevannet i Tromsø x timer etter midnatt
14. august 2018. 
""")

print("b) Bestem perioden til f. Gi en praktisk tolkning av svaret")
# legger inn funksjonen
a = 130
k = 0.501
c = -0.532
d = 148
vannstandTromsø = lambda x: a*sin(k*x-c)+d

x = linspace(0,24)
y = vannstandTromsø(x)
plt.plot(x,y)
plt.show()


periodeTromsø = 2*pi/k

print("Perioden er", periodeTromsø,". Det betyr at det er høyvann (og lavvann) hver", periodeTromsø,"time")

print("c) Gi en praktisk tolkning av tallene 148 og 130 i modellen f.")
print("148 er likevektslinjen. Det er midt mellom høyvann og lavvann.")
print("130 er amplituden. Det er avstanden mellom likevektslinjen og høyvann.")

print("d) Ved hvilke tidspunkter øker vannstanden med 50 cm per time?")

# deriverer numerisk
vannstandTromsøEndring = lambda x: derivative(vannstandTromsø,x,1e-6)

# finner ut når den deriverte er 50
fsolveResultat = fsolve(lambda x: vannstandTromsøEndring(x)- 50,0,full_output=True)

#lager en liste med løsningene
løsninger = []

# case 1: Ingen løsning
if fsolveResultat[2] != 1:
    print("Fant ingen løsning")

# case 2: Fant en løsning
# finner alle verdiene i intervallet
else:
    tidspuntkØkning50 = fsolveResultat[0][0]

    startverdi = 0
    sluttverdi = 24

    #må iterere både forover og bakover
    positivLøsning = tidspuntkØkning50
    while positivLøsning <= sluttverdi:
        print("p",positivLøsning)
        if positivLøsning > startverdi:
            løsninger.append(positivLøsning)
        positivLøsning = positivLøsning + periodeTromsø

    negativLøsning = tidspuntkØkning50 - periodeTromsø
    while negativLøsning >= startverdi:
        print("n",negativLøsning)
        if negativLøsning < sluttverdi:
            løsninger.append(negativLøsning)
        negativLøsning = negativLøsning - periodeTromsø

    if len(løsninger)==1:
        print("Vannstanden øker med 50 cm klokken", løsninger[0])
    else:
        print("Vannstanden øker med 50 cm per time klokkeslettene:", løsninger)
        
print("Tegner funksjonen og ser om vi har funnet alle løsningene:")

x = linspace(0,24,1000)
y = vannstandTromsøEndring(x)
plt.plot(x,y)
plt.plot([0,24],[50,50])
plt.show()
print("Vi finner bare en løsning, det er ingen vei utenom en analytisk løsning.")
verdi = 50
v = arccos(verdi/(a*k))
v1 =  (v-c)/k
v2 = (2*pi-v-c)/k
løsninger = []
while v1 < 24:
    løsninger.append(v1)
    v1 += periodeTromsø

while v2 < 24:
    løsninger.append(v2)
    v2 += periodeTromsø
    
løsninger.sort()
print("Løsninger :",løsninger)