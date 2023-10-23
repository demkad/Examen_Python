"""
Casus 2: Aanspreking met gebruik van een functie, afdruk gebruik vanuit de functie

De gebruiker geeft 3 keer de waarde van de functie in

· Aanspreking(geslacht,Familie_naam,beroep)

· Indien het geslacht M: Heer, Geslacht V: Mevrouw

· Titel, deze titels zijn gekend door het programma.

o Dokter: Dr.

o Professor: Prof.

o Ingenieur: Ir.

o Andere: Geen ansprekeing

§ Titels worden niet gecombineerd in deze opdracht.

· Voorbeeld output(Man,Peeters,Dokter): Geachte Heer Prof Peeters.
"""

# functies:
def aanspreking(g,n,b):
    if g.upper()=='M':                          # steek geslacht in variabele geslacht
        geslacht='Heer'
    else:
        geslacht='Mevrouw'
    if b.upper()=='DOKTER':                     # vervang beroep door overeenkomstige afkorting
        beroep='Dr.'
    elif b.upper()=='PROFESSOR':
        beroep='Prof.'
    elif b.upper()=='INGENIEUR':
        beroep='Ir.'
    else:
        beroep=''
    print('Geachte',geslacht,beroep,n)


# hoofdprogramma:
for i in range(3):
    n=input('Naam: \n')
    g=input('Geslacht? (M/V)\n')
    while g.upper() not in ['M','V']:
        g=input('Geslacht? M/V')                # Doublecheck voor g -> mag alleen maar m of v zijn anders gaat het programma niet verder
    b=input('Beroep? (Kies uit: Dokter, Professor, Ingenieur of andere)\n')
    aanspreking(g,n,b)
