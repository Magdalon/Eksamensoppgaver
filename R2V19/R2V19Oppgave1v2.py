# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:37:17 2019

@author: magdalon

Program som løser oppgave 1, del 2 fra eksamen i Matematikk R2 Vår 2019
"""

# laster inn nødvendige biblioteker
from numpy import array, isreal ,sin, arcsin, diff, linspace, pi, floor, abs, around, log10, cos, arccos
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

"""
Lager et trigonometriskFunksjon-objekt
Dette har sinusfunksjon og cosinusfunksjon som underklasser
Dette skal kunne:
    - definere de fire konstantene OK
    - regne ut funksjonsverdier OK
    - lagre start og sluttintervallet OK
    - tegne funksjonen OK
    - printe ut funksjonsuttrykket OK- Avrunder ikke riktig
    - finne x for en gitt y eller gi en feilmelding
    
    - finne de deriverte ved hjelp av
    - gi verdien til den deriverte i et punkt
    - tegne den deriverte
    - printe ut funksjonsuttrykket
    - finne x for en gitt y eller gi en feilmelding.

    - finne de fire konstantene med numerisk integrasjon
    - lagre regresjonsuttrykket
"""

def sigfig(x,n=3):
    xr = (floor(log10(abs(x)))).astype(int)
    xr=10.**xr*around(x/10.**xr,n-1)   
    return xr    

class TrigFunksjon(object):
    trig = None
    inverse = None
    @classmethod
    def generator (cls,x,amplitude,k,c,likevektslinje):
        return amplitude*cls.trig(k*x + c) + likevektslinje

    def __init__(self, amplitude, k,c,likevektslinje, fra = None, til = None, xVerdier = [], yVerdier = [],debug = True):
        self.amplitude = amplitude
        self.k = k
        self.c = c
        self.likevektslinje = likevektslinje
        self.fra = fra
        self.til = til
        self.funksjon = lambda x: self.generator(x,amplitude,k,c,likevektslinje)
        self.xVerdier = xVerdier
        self.yVerdier = yVerdier
        if debug:
            self.tegn()
            print(self.uttrykk())
            
    def __call__(self,x):
        return self.funksjon(x)

    def grenser(self,fra,til):
        if not fra:
            if self.fra:
                fra = self.fra
            else:
                fra = 0
        if not til:
            if self.til:
                til = self.til
            else:
                til = 2*pi/self.k
        return fra, til
   
    def tegn(self, fra=None, til=None, close=True):

        fra,til = self.grenser(fra,til)
        if len(self.xVerdier)>0:
            plt.plot(self.xVerdier,self.yVerdier,"p")
        x = linspace(fra,til,1000)
        y = self(x)

        plt.plot(x,y)
        if close:
            plt.show()
    
    def uttrykk(self):
        return "f(x) = {} {} ( {} x + {} ) + {}".format(*[self.amplitude,self.trig.__name__,self.k,self.c,self.likevektslinje])
    
    def periode(self):
        return 2*pi/self.k
    
    def løs(self,verdi,fra=None,til=None, debug = True):
        fra, til = self.grenser(fra,til)

        #lager en liste med løsningene
        løsninger = []

        # løser symbolsk
        fundamentalløsninger = (self.løsninger(verdi)-self.c)/self.k

        for løsning in fundamentalløsninger:
            #må iterere både forover og bakover
            positivLøsning = løsning
            while positivLøsning <= til:
                if positivLøsning >= fra:
                    løsninger.append(positivLøsning)
                positivLøsning = positivLøsning + self.periode()

            negativLøsning = løsning - self.periode()
            while negativLøsning >= til:
                if negativLøsning <= fra:
                    løsninger.append(negativLøsning)
                negativLøsning = negativLøsning - self.periode()
        
        løsninger.sort()
        
        if debug:
            self.tegn(fra,til,close = False)
            x = linspace(fra,til,2)
            y = [verdi,verdi]
            plt.plot(x,y)
            plt.show()
        return løsninger
    
        def __str__(self):
            return self.uttrykk()

        def __repr__(self):
            return self.uttrykk()

    @classmethod
    def tilpass(cls,xVerdier, yVerdier, fra = False, til = False,debug = True):
        if not isreal(fra):
            fra = min(xVerdier)
        
        if not isreal(til):
            til = max(xVerdier)
            
        # må finne en gjetning for a, b, c og d for å starte optimeringsprosedyren
        amplitudeGjett = (max(yVerdier)-min(yVerdier))/2  # amplituden er lett å regne ut
        likevektslinjeGjett = (max(yVerdier)+min(yVerdier))/2  # likevektslinjen er lett å regne ut

        # litt vanskeligere å finne b og c
        # k / 2pi = avstand mellom to punkter på grafen i samme fase...
        # k / pi  = avstand mellom toppunkt og bunnpunkt.

        # bruker at f'(x) er tilnærmet lik a*k når vi er på likevektslinjen. Da er den deriverte størst.
        # deriverer numerisk
        numeriskDerivert = diff(yVerdier)/diff(xVerdier)
        # finner den største verdien av den deriverte og  deler på a for å finne k
        kGjett = max(abs(numeriskDerivert))/amplitudeGjett
        
        # -c/k er det punktet hvor grafen krysser likevektslinjen for første gang. Setter dette til null
        cGjett = 0

        parametre, kovarianser = curve_fit(cls.generator,xVerdier, yVerdier, p0=[amplitudeGjett, kGjett, cGjett, likevektslinjeGjett])
        amplitude, k, c, likevektslinje = parametre
 
        if debug:
            print("Startverdier for iterasjon:")
            print("amplitude:",amplitudeGjett)
            print("k:",kGjett)
            print("c:",cGjett)
            print("likevektslinje:",likevektslinjeGjett)
            print()
          
            print("Sluttverdier for iterasjon:")
            print("amplitude:",amplitude)
            print("k:",k)
            print("c:",c)
            print("likevektslinje:",likevektslinje)

        nyFunksjon = cls(amplitude, k, c, likevektslinje, fra, til, xVerdier, yVerdier)

        return nyFunksjon


        
class Sinusfunksjon(TrigFunksjon):
    trig = sin
    inverse = arcsin

    def derivert(self):
        return Cosinusfunksjon(self.amplitude*self.k,self.k,self.c,0,self.fra,self.til)

    def løsninger(self,verdi):
        v = self.inverse((verdi-self.likevektslinje)/self.amplitude)
        return array([v,pi-v])
    


class Cosinusfunksjon(TrigFunksjon):
    trig = cos
    inverse = arccos

    def derivert(self):
        return Sinusfunksjon(-1*self.amplitude*self.k,self.k,self.c,0,self.fra,self.til)

    def løsninger(self,verdi):
        v = self.inverse((verdi-self.likevektslinje)/self.amplitude)
        return array([v,2*pi-v])

"""    
class Tangensfunksjon(TrigFunksjon):
    trig = cos
    inverse = arctan
    
    def derivert(self):
        return la

"""


"""
test = Sinusfunksjon(1,1,0,0,0,4*pi)

print(test.verdi(0))
test.tegn()
test.tegn(0,2*pi)
print(test.uttrykk())
print(test.løs(0))
"""
print(
"""
Oppgave 1 (6 poeng)

Tabellen nedenfor viser vannstanden til tidevannet ved Leirvik på Stord 14. august 2018.
Vannstanden er målt fra et nullnivå som heter sjøkartnull. 

Klokkeslett    03.00  06.00  09.00  12.00  15.00  18.00  21.00  23.00
Vannstand (cm)   102     26     10     81    109     43     20     57 
)
""")
print("a) Bruk tallene fra tabellen til å lage en sinusfunksjon g som er en god modell for vannstanden.")
# laster inn dataene
klokkeslett = [03.00,  06.00,  09.00,  12.00,  15.00,  18.00,  21.00,  23.00]
vannstand = [102, 26, 10, 81, 109, 43, 20, 57]
vannstandStord = Sinusfunksjon.tilpass(klokkeslett,vannstand,fra = 0, til = 24)

print("""Funksjonen f gitt ved
f(x) = 130 sin(0,501x - 0,532) + 148 
er en god modell for vannstanden til tidevannet i Tromsø x timer etter midnatt
14. august 2018. 
""")

print("b) Bestem perioden til f. Gi en praktisk tolkning av svaret")

vannstandTromsø = Sinusfunksjon(130,0.501,-0.532,148,0,24)

print("Perioden er", vannstandTromsø.periode(),". Det betyr at det er høyvann (og lavvann) hver", vannstandTromsø.periode(),"time")

print("c) Gi en praktisk tolkning av tallene 148 og 130 i modellen f.")
print("148 er likevektslinjen. Det er midt mellom høyvann og lavvann.")
print("130 er amplituden. Det er avstanden mellom likevektslinjen og høyvann.")

print("d) Ved hvilke tidspunkter øker vannstanden med 50 cm per time?")
vannstandTromsøEndring = vannstandTromsø.derivert()
tid = vannstandTromsøEndring.løs(50)

def klokkeslett(tid,start = 0):
    timer = int(tid)
    minutter = int(around(60*(tid % 1)))
   
    if (minutter == 60):
        timer += 1
        minutter = 00
    
    return "{:02d}.{:02d}".format(timer, minutter)


print("Vannet stiger med 50 cm i timen på klokkeslettene:",", ".join(list(map(klokkeslett,tid))))