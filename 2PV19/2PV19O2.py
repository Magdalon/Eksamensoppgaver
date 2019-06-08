# -*- coding: utf-8 -*-
#importerer funksjonene vi trenger
#importerer muligheten for å tegne grafer
import matplotlib.pyplot as plt

"""
Oppgave 2 (3 poeng)
Diagrammet nedenfor viser hvor mange minutter personer i ulike aldersgrupper brukte på å se på vanlig tv i gjennomsnitt i løpet av et døgn i 2015 og i 2017.
     2-11 år  12-19 år  20-29 år  30-39 år  40-49 år  50-64 år  65- år
2015: 80      67        119       146       175       212       252
2017: 52      46        78        111       134       191       260
Bruk opplysningene du kan lese ut av diagrammet ovenfor og lag to nye diagrammer.
* Det ene diagrammet skal vise endring i seertid i minutter for hver aldersgruppe fra 2015 til 2017.
* Det andre diagrammet skal vise endring i seertid i prosent for hver aldersgruppe
fra 2015 til 2017.
"""

# Det ene diagrammet skal vise endring i seertid i minutter for hver aldersgruppe fra 2015 til 2017.
# Oppskrift hentet fra https://python-graph-gallery.com/10-barplot-with-number-of-observation/
seertid15 = [80, 67, 119, 146, 175, 212, 252]
seertid17 = [52, 46, 78, 111, 134, 191, 260]
labels = ["2-11 år", "12-19 år", "20-29 år", "30-39 år", "40-49 år", "50-64 år", "65- år"]
endring = list(map(lambda x,y: x-y, seertid17, seertid15))

# Create barplot
plt.bar([1,2,3,4,5,6,7],endring,width = 0.9,label = "Endring i tv-bruk (minutter per døgn)")
# Create legend
plt.legend()
# Text below each barplot with a rotation at 90°
plt.xticks([r + 0.9 for r in range(len(endring))], labels,rotation = 90)
# Text on the top of each barplot
r=list(range(1,9))
for i in range(len(endring)):
    plt.text(x = r[i]-0.4, y = endring[i]-2, s = str(endring[i])+" min")
# Adjust the margins
plt.subplots_adjust(bottom= 0.2, top = 0.98)
# Show graphic
plt.show()

# * Det andre diagrammet skal vise endring i seertid i prosent for hver aldersgruppe fra 2015 til 2017.

prosentendring = list(map(lambda x,y: round(100*x/y), endring, seertid15))

# Create barplot
plt.bar([1,2,3,4,5,6,7],prosentendring,width = 0.9,label = "Endring i tv-bruk (prosent)")
# Create legend
plt.legend()
# Text below each barplot with a rotation at 90°
plt.xticks([r + 0.9 for r in range(len(prosentendring))], labels,rotation = 90)
# Text on the top of each barplot
r=list(range(1,9))
for i in range(len(endring)):
    plt.text(x = r[i]-0.4, y = prosentendring[i]-2, s = str(prosentendring[i])+" %")
# Adjust the margins
plt.subplots_adjust(bottom= 0.2, top = 0.98)
# Show graphic
plt.show()