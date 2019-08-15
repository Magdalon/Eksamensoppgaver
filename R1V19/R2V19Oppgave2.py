# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:17:05 2019

@author: magdalon
"""

import scipy.stats as sps

print("""
Oppgave 2 (5 poeng)
På en arbeidsplass er det tolv kvinner og åtte menn. Hver måned arrangerer de et lotteri. Det går ut på at alle legger en lapp med navnet sitt i en eske. De trekker så ut tre tilfeldige lapper fra esken. Lappene legges ikke tilbake mellom hver gang de trekker. De tre som blir trukket ut, vinner en kinobillett hver.
""")

print("""
a) Vis at sannsyngligheten er p \approx 0.2947 for at nøyaktig to av de tre vinnerne er menn.
""")

kvinner = 12
menn = 8
utvalg = 3

hypergeometriskFordeling = sps.hypergeom(menn +kvinner,menn,utvalg)
p = hypergeometriskFordeling.pmf(2)

print("Svar:",p)

print("""
I løpet av et år arrangerer de tolv slike lotterier.

b) Bestem sannsynligheten for at nøyaktig to av vinnerne er menn i seks av de tolv lotteriene.
""")

måneder = 12
binomiskFordeling = sps.binom(måneder,p)
p1 = binomiskFordeling.pmf(6)
print("Svar:",p1)
print("""
c) Bestem sannsynligheten for at de tre vinnerne har samme kjønn i minst ett av de tolv lotteriene.
""")

sannsynlighetUliktKjønn = hypergeometriskFordeling.pmf(1) + hypergeometriskFordeling.pmf(2)

sannsynlighetUliktKjønnHverMåned = sannsynlighetUliktKjønn**måneder

sannsynlighetMinstEnLiktKjønn = 1-sannsynlighetUliktKjønnHverMåned

print("Svar:",sannsynlighetMinstEnLiktKjønn)

