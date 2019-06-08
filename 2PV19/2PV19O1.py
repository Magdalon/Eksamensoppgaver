# Først må vi importere de funksjonene vi trenger
# importerer muligheten til å tegne grafer
import matplotlib.pyplot as plt
#importerer numpy
import numpy as np
# importerer scipy-funksjoner
from scipy.optimize import fsolve
from scipy.misc import derivative

print("Eksamen Matematikk 2P Vår 2019: Oppgave 1 Del 2")
print()

print("Et firma produserer vanntanker. Carl har undersøkt en av tankene og funnet ut at dersom tanken er full og kranen pånes, vil det etter x minutter være V(x) liter vann igjen i tanken, der V(x) = (10-0.1x^2)^3, 0 <= x <= 10")
print()

print("a) Bestem V(0) og gi en praktisk tolkning av svaret du får.")

# Vi ser at vi skal bruke V(x) flere ganger, så vi lager en funksjon. 
# Vi gir variabelen x og funksjonen V(x) forklarende navn.
# Dette er god programmeringsskikk [cite]

def restmengde(tid):
    return (10-0.1*tid**2)**3
print("V(0) =",restmengde(0))
print("Dette betyr at tanken rommer",restmengde(0), "liter")

print()

print("b) Bruk graftegner til å tegne grafen til V.")

# Her bruker jeg graftegningsmulighentene i pakken matplotlib som følger med Anaconda3
# Oppskrift hentet fra https://glowingpython.blogspot.com/2011/04/how-to-plot-function-using-matplotlib.html

tidMin = 0
tidMax = 10
fig = plt.figure()
ax = plt.axes()
tidspunkt= np.linspace(tidMin,tidMax,(tidMax-tidMin)*100)
plt.plot(tidspunkt,restmengde(tidspunkt))
plt.show()

print()

print("c) Hvor lang tid går det fra kranen åpnes, til det er 400 L vann igjen i tanken?")

# Her må vi finne nullpunkt.
# bruker optimeringspakken i SciPy (Inkludert når vi laster ned Anaconda 3)
# fsolve finner nullpunkt. Vi må derfor skrive om uttrykket vårt fra
# restmengde(tid)=400
# til 
# restmengde(tid)-400 =0
# og lagre venstresiden som en ny funksjon
# vi trenger også å vite hvor vi skal starte løsningsprosedyren,
# ser av grafen at 5 ser ut til å være et godt utgangspunkt
# Oppskrift hentet fra: https://docs.scipy.org/doc/scipy/reference/optimize.nonlin.html

func = lambda x : restmengde(x)-400
start = 5
svar = fsolve(func,start)
print("Det er 400 liter igjen på tanken etter", svar[0], "minutter!")

print()

print("d) Hvor mye vann renner i gjennomsnitt ut av tanken per minutt mens den tømmes?")

    # Her har jeg hatt minus foran gjennomsnittlig vekstfart fordi den måler hvor fort
# noe vokser, for å finne ut hvor fort noe minker må jeg skifte fortegn

gjennomsnittligVekstfart = (restmengde(tidMax)-restmengde(tidMin))/(tidMax-tidMin)
print("Det renner gjennomsnittlig ut ",-gjennomsnittligVekstfart," liter per minutt")


print()

print("e) Bestem den momentane vekstfarten til funksjonen V når x=3. Gi en praktisk tolkning av svaret du får")
    
# her må vi derivere numerisk
# dette gjør vi ved å regne ut (f(x+dx)-f(x-dx))/2dx
# hvor dx er et 'lite' tall, typisk 10^-6

#Oppskrift hentet fra: https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.misc.derivative.html")
    
momentanVekstfart = derivative(restmengde,3,1e-6)
print("Den momentane vekstfarten er", momentanVekstfart) 
#for å si om den stiger eller synker må vi se på fortegnet.
retning = {1:"STIGER",-1:"SYNKER"}
print("Dette betyr at vannmengden", retning[np.sign(momentanVekstfart)],"med", abs(momentanVekstfart)," liter per minutt")

print()
