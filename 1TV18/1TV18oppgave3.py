# -*- coding: utf-8 -*-

# laster inn muligheten til å tegne
import matplotlib.pyplot as plt

# laster inn muligheten til å tegne venndiagram
from matplotlib_venn import venn2

print("Oppgave 3")
print("a) Systematiser opplysningene i en krysstabell eller et venndiagram")
print("Oppskrift hentet fra: 'https://python-graph-gallery.com/venn-diagram/'")
print("Modulen 'matplotlib_venn' hentet fra: https://anaconda.org/conda-forge/matplotlib-venn. Skriv inn 'conda install -c conda-forge matplotlib-venn ' i kommandolinjen for å laste ned")
kunder = 450
popcorn = 280
smågodt = 220
ingenting = 30

snitt = 220-(450-280-30)

venn2(subsets=(popcorn,smågodt,snitt),set_labels=("Popcorn","Smågodt"))
plt.show()

print("b) Bestem sannsynligheten for at en tilfeldig valgt kunde kjøpte både popcorn og smågodt.")
p=snitt/kunder
print("Sannsynligheten er p="+str(p))


print("c) En kunde kjøpte smågodt. Bestem sannsynligheten for at kunden ikke kjøpte popcorn.")  
p = 1-snitt/smågodt
print("Sannsynligheten er p="+str(p))