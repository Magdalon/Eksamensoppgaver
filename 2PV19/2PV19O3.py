# -*- coding: utf-8 -*-
'''
Oppgave 3 (3 poeng)
Det er 5,3 millioner innbyggere i Norge. I gjennomsnitt kaster hver innbygger 180 plastposer hvert år. Normal tykkelse på plasten i en pose er 0,035 mm.
Tenk deg at vi legger alle disse plastposene oppå hverandre i en stabel.
a) Omtrent hvor høy ville stabelen blitt?
b) Eiffeltårnet i Paris er 324 m høyt. Hvor mange timer ville det gå før stabelen var like høy som Eiffeltårnet, dersom vi antar at det kastes like mange poser hver time?
'''

# a) Omtrent hvor høy ville stabelen blitt?

nordmenn = 5.3e6
plastposerPerNordmenn = 180
plastposetykkelse =0.035e-3
høyde = nordmenn*plastposerPerNordmenn*plastposetykkelse*2
print("Stabelen ville blitt", høyde, "meter høy")

# b) Eiffeltårnet i Paris er 324 m høyt. Hvor mange timer ville det gå før stabelen var like høy som Eiffeltårnet, dersom vi antar at det kastes like mange poser hver time?

eifeltårn = 324
årstimer = 365*24
vekstfart = høyde/årstimer
tid = eifeltårn/vekstfart
print("Det tar", tid, " timer før stabelen er like høy som eifeltårnet.")