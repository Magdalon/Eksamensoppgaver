# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:50:05 2019

@author: magdalon
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print("""
Oppgave 2 (3 poeng)
På en øy ble det satt ut 50 harer. Tabellen nedenfor viser hvor mange harer det var på
øya etter 0, 10, 20 og 30 uker.
Antall uker etter utsettingen   0    10   20   30
Antall harer                    50  104  156  184 

Antall harer på øya t uker etter at harene ble satt ut, kan ifølge en forsker modelleres
med en funksjon g på formen 

g(t) = N/(1+a*e**(-kt))
""")

print("""
a) Bruk regresjon til å bestemme N, a og k.
""")

tid = [0,10,20,30]
harer = [50,104,156,184]

def sigmoid(x,N,a,k):
    return N/(1+a*np.exp(-k*x))
p0 = [max(harer), max(harer)/min(harer), np.log(max(harer)/max(tid))]
params, variance =curve_fit(sigmoid,tid,harer,p0=p0)
N,a,k = params

plt.plot(tid,harer,"o")
interval = max(tid)-min(tid)
xs = np.linspace(min(tid) -0.2*interval,max(tid)+0.2*interval,1000)
ys = sigmoid(xs,N,a,k)
plt.plot(xs,ys)
plt.plot([min(xs),max(xs)],[N,N],"r")
plt.show()
print("g(t) =", N,"/(1+",a,"*e**(-,",k,"*t))")

print("""
b) Hvilken informasjon gir tallet N i denne situasjonen?
""")

print("Svar: N er grenseverdien når tiden går mot uendelig")