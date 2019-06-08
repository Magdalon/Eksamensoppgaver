# -*- coding: utf-8 -*-

# laster inn muligheten til å tegne
import matplotlib.pyplot as plt
# laster inn numpy
import numpy as np

print("Oppgave 1")
print("a) Bruk graftegner til å tegne grafen til h for x mellom 0 og 12")
# Definerer først funksjonen
def h(x):
    return -0.07*x**2+0.67*x+2.04

print("Oppskrift hentet fra 'https://glowingpython.blogspot.com/2011/04/how-to-plot-function-using-matplotlib.html'")

fig = plt.figure()
ax = plt.axes()
x= np.linspace(0,12,1200)
plt.plot(x,h(x))
plt.show()


print("b) Vil ballen gå over nettet?")
banelengde = 18
midtpunkt = banelengde/2
netthøydeKvinner=2.24
netthøydeMenn=2.43
print("Ballen vil gå over nettet, dersom høyden er større enn netthøyden når vi er midt på banen")
print("Høyde over nettet", h(midtpunkt))

# her har vi et eksempel på en logisk test.

if h(midtpunkt)>netthøydeMenn:
    print("Ballen vil gå over mennenes nett")
else: 
    print("Ballen vil ikke gå over mennenes nett")
    
if h(midtpunkt)>netthøydeKvinner:
    print("Ballen vil gå over kvinnenes nett")
else:
    print("Ballen vil ikke gå over kvinnenes nett")

print("")