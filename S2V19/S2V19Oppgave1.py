# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:38:48 2019

@author: magdalon
"""

from sympy import *

print("""
Oppgave 1 (3 poeng)

En sjørøverskatt har mynter med verdiene 1, 5 og 10 skilling. Myntene veier henholdsvis
5 g, 8 g og 12 g. Du får vite at
* skatten inneholder 85 mynter
* den samlede verdien er på 356 skilling
* den samlede vekten er 633 g     
""")

print("""
a) Bruk opplysningene til å sette opp tre likninger med tre ukjente. 
""")

A=Matrix([[1,1,1],[1,5,10],[5,8,12]])
b = Matrix([85,356,633])

print("""
b) Bruk CAS til å løse likningssystemet du satte opp i oppgave a). 
""")
x,y,z = symbols("x y z")
svar = linsolve((A,b), [x,y,z])
print("Svar:",svar)