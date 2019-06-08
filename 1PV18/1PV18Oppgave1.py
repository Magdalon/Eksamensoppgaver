# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:03:34 2019

@author: magopda
"""
#importerer numpy
import numpy as np

#importerer muligheten til å tegne
import matplotlib.pyplot as plt

#importerer  muligheten til å løse likheter numerisk


print("Oppgave 1")
print("a) Bruk graftegner til å tegne grafen til T(x)")
def T(x):
    return -0.018*x**3+0.55*x**2-3.5*x+13

Txmin = 0
Txmax = 20
print("Oppskrift hentet fra 'https://glowingpython.blogspot.com/2011/04/how-to-plot-function-using-matplotlib.html'")

fig = plt.figure()
ax = plt.axes()
x= np.linspace(Txmin,Txmax,(Txmax-Txmin)*100)
plt.plot(x,T(x))
plt.show()
print("")

print("b) På hvilke tidspunkt (klokkeslett) var temperaturen 10 grader?")
print("Løser ligningen T(x) - 10= 0 ved hjelp av 'numpy.roots(<liste med polynomkooeffisienter>)")
print("Fremgangsmåte fra: 'https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.roots.html'")

#når vi skal skrive ut svaret må vi ta vekk løsninger som ikke er i intervallet
Tk = [-0.018,0.55,-3.5,3] #koeffisientene i polynomuttrykket
tidspunkt = np.roots(Tk)
tidspunktDF = list(filter(lambda x: (x>Txmin and x <Txmax),tidspunkt))
print("Temperatur 10 grader: " + str(tidspunktDF))

print("")

print("c) Bestem forskjellen mellom høyeste og laveste temperatur i perioden fra midnatt og fram til klokka 20.")
dTk = np.poly1d(Tk).deriv()
ekstremalTidspunkt = np.roots(dTk)
ekstremalTidspunktDF = list(filter(lambda x: (x>Txmin and x <Txmax),ekstremalTidspunkt))
np.append(ekstremalTidspunkt,[Txmin,Txmax])
ekstremalkandidater = T(ekstremalTidspunkt)

størsteForskjell = max(ekstremalkandidater) - min(ekstremalkandidater)
print("Største forskjell: "+ str(størsteForskjell))
