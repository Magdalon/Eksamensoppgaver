# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:22:22 2019

@author: magdalon
"""

import scipy.stats as sps

print("""
Oppgave 3 (8 poeng)

På en arbeidsplass er det tolv kvinner og åtte menn. Hver måned arrangerer de et lotteri. Det foregår på den måten at alle legger én lapp med navnet sitt på i en eske. De trekker så ut tre tilfeldige lapper fra esken. Lappene legges ikke tilbake mellom hver gang de trekker. De tre som blir trukket ut, vinner en kinobillett hver. 
""")
print("""
a) Vis at sannsynligheten er p = 0.2947 for at nøyaktig to av de tre vinnerne er menn. 
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
c) Bestem sannsynligheten for at flertallet av vinnerne er kvinner i minst halvparten av
lotteriene.      
""")

sannsynlighetFlertallKvinner = hypergeometriskFordeling.pmf(0) + hypergeometriskFordeling.pmf(1)

binomiskFordeling = sps.binom(måneder,sannsynlighetFlertallKvinner)

sannsynlighetMinstSeksGanger = 1-binomiskFordeling.cdf(5)

print("Svar:",sannsynlighetMinstSeksGanger)
print("""
d) Bestem sannsynligheten for at de tre vinnerne har samme kjønn i minst ett av de tolv lotteriene.
""")

sannsynlighetUliktKjønn = hypergeometriskFordeling.pmf(1) + hypergeometriskFordeling.pmf(2)

sannsynlighetUliktKjønnHverMåned = sannsynlighetUliktKjønn**måneder

sannsynlighetMinstEnLiktKjønn = 1-sannsynlighetUliktKjønnHverMåned

print("Svar:",sannsynlighetMinstEnLiktKjønn)

