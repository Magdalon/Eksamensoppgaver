# -*- coding: utf-8 -*-

# Importerer biblioteker
# Importerer NumPy
import numpy as np

# Emil og Ida selger poser med brente mandler for å samle inn penger i forbindelse med
# Operasjon Dagsverk. Begge har fylt 20 poser med mandler.
# Nedenfor ser du hvor mange mandler det er i hver av posene Emil har fylt.
# 42 45 39 46 47
# 41 38 44 43 40
# 45 46 49 39 40
# 41 42 40 45 48
# a) Bestem gjennomsnittet og standardavviket for antallet mandler i posene til Emil.
# Vi lager først en array (liste) med antall mandler i posene.
# Så bruker vi NumPy-funksjonene mean() for å regne ut gjennomsnitt,
# og np.std() for å regne ut gjennomsnitt. 
mandler = [42, 45, 39, 46, 47, 41, 38, 44, 43, 40, 45, 46, 49, 39, 40, 41, 42, 40, 45, 48]
gjennomsnitt = np.mean(mandler)
standardavvik = np.std(mandler)

print("Gjennomsnittet er",gjennomsnitt,"mandler")
print("Standardavviket er",standardavvik,"mandler")

# Ida har regnet ut gjennomsnitt og standardavvik for antall mandler i sine poser
# Gjennomsnittet hennes er lavere enn Emils, men standardavviket er høyere.
# b) Nedenfor ser du tre påstander. Avgjør om hver enkelt påstand kan være riktig.
# Begrunn svarene dine.
# 1) Ida har til sammen flere mandler enn Emil i posene sine.
# Kan ikke være riktig. Siden gjennomsnitt er sum/antall, og de har likt antall,
# må summen til Ida være lavere.
# 2) Ida har like mange mandler i hver av posene sine.
# Kan ikke være riktig. Siden standardavviket hennes er høyere må det være 
# mer variasjon i antall mandler i posene hos ida
# 3) Ida har like mange mandler i halvparten av posene sine.
# Kan være riktig, vi kjenner ikke fordelingen av mandlene i posene til
# Ida, standardavvik og gjennomsnitt sier bare noe om alle posene, ikke
# en del av posene....