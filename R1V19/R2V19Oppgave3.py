# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:08:51 2019

@author: magdalon
"""

from sympy import *
from functools import reduce

print("""
Oppgave 3 (8 poeng)

Funksjonen f er gitt ved

    f(x) = x^3 + 4x^2 + 4x + 2
""")

print("a) Bruk graftegner til å tegne grafen til f.")
x = symbols('x')
f = x**3 + 4*x**2 + 4*x + 2
nullpunkt = list(solveset(f,x).intersect(S.Reals).evalf())
ekstremalpunkt = list(solveset(diff(f),x).intersect(S.Reals).evalf())
vendepunkt = list(solveset(diff(diff(f)),x).intersect(S.Reals).evalf())
punkter = [0]+nullpunkt + ekstremalpunkt + vendepunkt

interval = max(punkter)-min(punkter)
start = min(punkter)-0.1*interval
slutt = max(punkter) + 0.1*interval

plot(f,(x,start,slutt))

print("""
b) Bestem eksakte verdier for koordinatene til eventuelle toppunkt, botnpunkt og vendepunkt på grafen til f.""")
print("Nullpunkt:",nullpunkt)
print("Vendepunkt:",vendepunkt)
#Skiller topp og bunnpunkt med andrederiverttesten
toppunkt = []
bunnpunkt = []
sadelpunkt = []
for kandidat in ekstremalpunkt:
    andrederivert = diff(diff(f)).subs({x:kandidat})
    if andrederivert > 0:
        bunnpunkt.append(kandidat)
    elif andrederivert < 0:
        toppunkt.append(kandidat)
    else:
        sadelpunkt.append(kandidat)
        
print("Toppunkt:",toppunkt)
print("Bunnpunkt:",bunnpunkt)
print("Sadelpunkt:",sadelpunkt)

print("""
Funksjonen g er gitt ved
     
      g(x) = x**3 + a*x**2+4*x+2
      
c) Bruk CAS til å avgjøre for hvilke verder av a grafen til g har både et toppunkt og et bunnpunkt.
""")

a = symbols("a",real = True)
g = x**3 + a*x**2+4*x+2
print("Ligning for ekstremalpunkt:",Eq(diff(g,x),x))
svar = solveset(diff(g,x),x)
print("Utrykk for x-verdi til ekstremalpunkt:",svar)
e1, e2 = list(map(im,list(svar)))
plot(e1,e2)
# vi kan finne Punktene hvor imaginærdelen blir null: 
grenser1 = solve(e1,a)
grenser2 = solve(e2,a)
grenser1.sort()
# men er den ikke null inni eller utenfor intervallet?
# her må vi egentlig bevise at exp er kontinuerlig i det komplekse planet
# velger en verdi inni intevallet
indre = (max(grenser1)+min(grenser1))/2

if reduce(lambda x,y: x*y,map(lambda x,y: x.equals(y),grenser1,grenser2)):
    if e1.subs({a:indre}) > 0:
        print("a<",grenser1[0],"og",grenser1[1],"<a")
    else:
        print(grenser1[0],"< a <",grenser1[1])