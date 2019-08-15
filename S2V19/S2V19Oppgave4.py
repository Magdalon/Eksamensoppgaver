# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:02:55 2019

@author: magdalon
"""

print("""
Oppgave 4 (6 poeng)
Pia vurderer å låne 800 000 kroner. En bank tilbyr henne et annuitetslån med en
nedbetalingstid på 20 år, én termin per år og en fast rentesats på 3,0 % per år. Første
innbetaling er om ett år. 
""")

print("""
a) Sett opp en geometrisk rekke som kan brukes til å bestemme terminbeløpet.
Bruk CAS til å bestemme terminbeløpet.
""")
lånebeløp =800000
rentefot = 0.03
terminbeløpAnnuitet = lånebeløp/sum(map(lambda i: 1/(1+rentefot)**i,range(1,20)))

print("Terminbeløpet blir på", terminbeløpAnnuitet,"kr")

print("""
Banken tilbyr henne også et serielån med en nedbetalingstid på 20 år, én termin per år
og en fast rentesats på 3,0 % per år. Tabellen nedenfor viser avdrag, renter, terminbeløp
og restlån for de tre første terminene. 

Termin  Avdrag  Renter  Terminbeløp  Restlån
     1  40 000  24 000       64 000  760 000
     2  40 000  22 800       62 800  720 000
     3  40 000  21 600       61 600  680 000 

b) Forklar at terminbeløpene danner en aritmetisk følge.
Bestem summen av de 20 terminbeløpene for dette serielånet. 
""")

terminbeløpSerie = lambda i:65200-1200*i
lånekostnad = sum(map(terminbeløpSerie,range(1,20)))
print("Summen av terminbeløpene blir", lånekostnad, "kr")

print("""
En annen bank tilbyr henne et serielån på 800 000 kroner. Dette lånet har en
nedbetalingstid på 20 år, én termin per år og en fast rentesats per år. Summen av alle
terminbeløpene for dette lånet blir 1 000 000 kroner.
c) Bestem den faste rentesatsen per år for dette lånet.       
""")

lånekostnad = 1000000
terminer = 20
avdrag = lånebeløp/terminer

rentesats = (lånekostnad - lånebeløp)/sum(map(lambda i: lånebeløp - i*avdrag,range(0,19)))

print("Den faste rentesatsen er på ", rentesats*100,"%")