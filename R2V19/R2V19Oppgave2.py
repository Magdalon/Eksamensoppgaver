# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:39:29 2019

@author: magopda
"""
# importerer
from sympy import *
# setter opp
init_printing(use_unicode=True)
print("""
Oppgave 2 (7 poeng)
Punktene P(2, 4, -3) og Q(0, 0, 1) ligger på en kuleflate K slik at PQ er en diameter til
kuleflaten. 
""")

print("""
a) Vis at kuleflaten K er gitt ved likningen
(x-1)**2+(y-2)**2+(z+1)**2=9
""")

P = Point(2,4,-3)

Q = Point(0,0,1)
linjestykke = Segment(Q,P)
radius = linjestykke.length/2
sentrum = linjestykke.midpoint

x,y,z = symbols("x y z")

vs = Segment(sentrum,Point(x,y,z)).length**2
print(Eq(vs,radius**2))

print("""
Planet \alpha er gitt ved

\alpha: x-y+z=7

b) Bestem eksakt den minste avstanden mellom kuleflata K og planet \alpha.       
""")

alpha = Plane((7,0,0),(0,-7,0),(0,0,7))

sentrumsavstand = alpha.distance(sentrum)

overflateavstand = sentrumsavstand - radius 

print("Svar:",overflateavstand)

print("""Et plan \beta er gitt ved ligningen

\beta: 2x+y+t*(z-3)=-1

c) Vis at avstanden mellom sentrum i kuleflata K og planet \beta er gitt ved
""")

#d(t) = \frac{abs(5-4t)}{\sqrt{5+t^2}}

t = symbols("t")

exp = 2*x+y+t*(z-3)+1


ex = t
beta = Plane(Point3D( 0 , -1 ,3), Point3D(-0.5,0,3),Point3D(0,0,3-t**-1))

# Den innebygde avstandfunksjonen takler ikke symbolske koeffisienter.

k = beta.equation(x,y,z).expand()
a, b, c = [k.coeff(i) for i in (x, y, z)]
d = k.xreplace({x: sentrum.x, y: sentrum.y, z: sentrum.z})
avstand = sqrt(d**2/(a**2 + b**2 + c**2))

print("Svar:",avstand)

vis = Abs(5-4*t)/sqrt(5+t**2)

plot(vis,avstand)

print(""")
d) Bestem eksakte verdier for t slik at planet  tangerer kuleflaten K . """)

løsninger = solveset(Eq(avstand,radius),t)

print("Svar:",løsninger)
