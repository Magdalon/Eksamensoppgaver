# -*- coding: utf-8 -*-
# importerer dataene vi trenger
# importerer reduce
from functools import reduce
# importerer NumPy
import numpy as np
# importerer muligheten til å tegne grafer
import matplotlib.pyplot as plt
"""
Oppgave 8 (8 poeng)
Etter et arveoppgjør fikk Petter utbetalt 850 000 kroner. Den 1. januar 2008 opprettet han en sparekonto og satte inn hele beløpet på denne kontoen. Han bestemte seg for at pengene skulle stå urørt i banken i ti år.
Han fikk da to ulike tilbud fra banken.
Tilbud 1: En fast årlig rentesats på 4 % per år disse ti årene.
Tilbud 2: En rentesats som ville endres én gang per år i tråd med svingninger i
pengemarkedet. Det første året ville rentesatsen bli satt til 5,4 %.

a) Hvor mye hadde Petter til sammen fått i renter i løpet av de ti årene om han hadde valgt tilbud 1?

Petter valgte tilbud 2. I regnearket nedenfor ser du hvilken rentesats han fikk hvert år de ti årene.

5,4  3,5  2,3  2,4  2,2  2,2  2,1  1,6  1,2  1,1 

b) Lag en tabell i et regneark som vist til høyre. Legg inn opplysningene i de hvite cellene. I de blå cellene skal du sette inn formler.

c) Lag en ny tabell i regnearket fra oppgave b). Den nye tabellen skal vise hvor mye Peter hadde fått i renter hvert år om han hadde valgt tilbud 1.

d) Bruk tabellen fra oppgave c) til å bestemme hva den faste rentesatsen i tilbud 1 måtte ha vært for at Petter til sammen skulle fått like mye renter ved å benytte seg av dette tilbudet som han fikk ved å benytte seg av tilbud 2.

e) Bruk graftegner til å tegne grafen til funksjonen f gitt ved
$latex f(x)= 850000*x^10$
Vis hvordan du kan bruke den grafiske framstillingen til å komme fram til svaret du fikk i oppgave d).
"""

# a) Hvor mye hadde Petter til sammen fått i renter i løpet av de ti årene om han hadde valgt tilbud 1?
# lager verdifunksjon
startbeløp = 850000
rente = 4
tid = 10

def bankkonto(startbeløp,rente,tid):
    vekstfaktor = 1+rente/100
    return startbeløp*vekstfaktor**tid

sumRenter = bankkonto(startbeløp, rente, tid) - startbeløp
print("Han ville fått",sumRenter,"kr i renter")
print()
#b) Lag en tabell i et regneark som vist til høyre. Legg inn opplysningene i de hvite cellene. I de blå cellene skal du sette inn formler.
# det er mange måter å gjøre det på, vi kan regne ut linje for linje nedover og skrive ut svaret
# siden vi skal gjøre det flere ganger lager vi en funksjon


def spareInfo(startbeløp,renter,startår=0):
    nåværendeBeløp = startbeløp
    sumRenter = 0
    år = startår
    for r in renter:
        print("År:",år)
        print("Før renter:",nåværendeBeløp)
        rente = nåværendeBeløp*r/100
        sumRenter = sumRenter + rente
        print("Renter:",rente)
        nåværendeBeløp = nåværendeBeløp+rente
        print("Etter renter: ", nåværendeBeløp)
        print()
        år = år+1
    print("Sum renter:",sumRenter)     
    return nåværendeBeløp

renter2 = [5.4, 3.5, 2.3, 2.4, 2.2, 2.2, 2.1, 1.6, 1.2, 1.1]
sluttbeløp2 =spareInfo(startbeløp,renter2,2008)

print()

#c) Lag en ny tabell i regnearket fra oppgave b). Den nye tabellen skal vise hvor mye Peter hadde fått i renter hvert år om han hadde valgt tilbud 1.
# Vi lager en liste med rente hvert år
# Vi putter denne listen inn i funksjonen fra b
renter1 = [rente]*tid
spareInfo(startbeløp,renter1,2008)

# d) Bruk tabellen fra oppgave c) til å bestemme hva den faste rentesatsen i tilbud 1 måtte ha vært for at Petter til sammen skulle fått like mye renter ved å benytte seg av dette tilbudet som han fikk ved å benytte seg av tilbud 2.
# Vi må først regne ut den samlede vekstfaktoren for alternativ b, og siden regne
# ut hvilken rente det tilsvarer
# Det er ikke noen funksjon for n-te rot i python vi må bruke at n-te roten til et tall
# kan skrives som tall^(1/n)
vekstfaktorer2 = map(lambda x: 1+x/100,renter2)
vekstfaktor2 = reduce(lambda x,y:x*y,vekstfaktorer2)
vekstfaktor2år = vekstfaktor2**(1/tid)
rente2år = (vekstfaktor2år-1)*100
print("Renten måtte ha vært på",rente2år,"%")
print()
# e) Bruk graftegner til å tegne grafen til funksjonen f gitt ved
# $latex f(x)= 850000*x^10$
# Dette er en funksjon som gir oss sparebeløpet etter 10 år med x som veksfaktor
# Vekstfaktoren i vårt eksempel ligger mellom 1 og 1.05. Vi tegner mellom disse
# to verdiene
def f(x):
    return startbeløp*x**10
start = 1
slutt = 1.06
fig = plt.figure()
ax = plt.axes()
tidspunkt= np.linspace(start,slutt,(slutt-start)*1000)
plt.plot(tidspunkt,f(tidspunkt))
plt.show()

# Vis hvordan du kan bruke den grafiske framstillingen til å komme fram til svaret du fikk i oppgave d).
# Vi må finne ut når grafen vår krysser sluttbeløp for tilbud 2.
konstant = [sluttbeløp2]*int((slutt-start)*1000)
fig = plt.figure()
ax = plt.axes()
tidspunkt= np.linspace(start,slutt,(slutt-start)*1000)
plt.plot(tidspunkt,f(tidspunkt))
plt.plot(tidspunkt,konstant,color="red")
plt.show()

# Vi ser at grafene krysser litt over 1.02. Dette stemmer med svaret fra d.