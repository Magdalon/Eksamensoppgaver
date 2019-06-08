# -*- coding: utf-8 -*-
# Først må vi importere de funksjonene vi trenger
# importerer NumPy
import numpy as np

print("Oppgave 4")
print("Forskere har målt og veid laks i et område. Tabellen endenfor viser sammenhørende verdier av lengde og vekt")
print("Laksens lengde (cm) 50   60   70   80   90   100   105")
print("Laksens vekt (gram) 1290 2190 3470 5110 7450 10260 11950")

print("Anta at sammenhengen mellom laksens lengde x cm og vekt V gram kan beskrives med en modell av typen:")
print("V(x) = a*x^b")

print("a) Bruk datameterialet i tabellen til å bestemme tallene a og b.")
# Henter oppskriften fra https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# Vi bruker at vi kan ta logaritmen på begge sider og skrive
# log(V) = log(a*v^b)
# log(V) = log(a)+b^log(x) 

lengde = [50,60,70,80,90,100,105]
vekt = [1290, 2190, 3470, 5110, 7450, 10260, 11950]
fit = np.polyfit(np.log(lengde),np.log(vekt),1)
b = fit[0]
a = np.exp(fit[1])
print("a =", a)
print("b =", b)
print("V(x) = ",a,"*x^",b)

print("b) Bruk modellen du nå har funnet til å bestemme hvor mange prosent vekten på lanksen øker med når lengden øker med 25%")
# bruker logaritmeregler til å finne at
# vf = V(1.25x)/V(x) = (a*1.25x^b)/(a*1.25x^b)=1.25^b

vekstfaktorLengde = 1+25/100
vekstfaktorVekt = vekstfaktorLengde**b
prosentfaktorVekt = vekstfaktorVekt-1
prosentVekt = prosentfaktorVekt*100
print("En laks som er 25% større er",prosentVekt,"% tyngre")