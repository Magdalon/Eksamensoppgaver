# -*- coding: utf-8 -*-
# importerer regresjonsfunksjonen fra SciPy
from scipy.optimize import curve_fit

# Oppgave 5
# En butikk skal ha nattåpent fra klokka 20.00 til klokka 02.00. Eieren har bestemt seg for
# å selge et utvalg bukser til lavere og lavere priser utover kvelden og natten. 
# tid   0    1    2    3    4 
# pris  800  400  200  100  50
# Ovenfor ser du grafen til en eksponentialfunksjon . Grafen viser prisen for en
# bukse x timer etter klokka 20.00.


# b) Bestem funksjonsuttrykket til f.

# Finner først funksjonssuttrykket til f
# Vi gjetter på at dette er en eksponentialfunksjon, siden prisendringen
# ser ut til å være 50% per time
# først lager vi en funksjon som vi skal tilpasse, så gjør vi regresjon
# Oppskriften er hentet fra https://plot.ly/matplotlib/exponential-fits/

tid = [0,1,2,3,4]
pris=[800,400,200,100,50]

def eksponentialfunksjon(x,a,k):
    return a*k**x

fit = curve_fit(eksponentialfunksjon,tid,pris,p0=[800,0.5])

a = fit[0][0]
k = fit[0][1]
print("a=",a)
print("k=",k)
print("f(x)=",a,"*",k,"^x")

# a) Hvor mye vil en bukse koste når butikken stenger klokka 02.00?
# 02.00 er 6 timer etter 20.00
pris02=eksponentialfunksjon(6,800,0.5)
print("Buksen koster",pris02,"kr når butikken stenger")

