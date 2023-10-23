"""
Casus 3:Fietsverhuur.

· De gebruiker geeft in hoeveel fietsen hij wenst te huren(hoofdprogramma). Per fiets wordt er een kostprijs berekend. De berekening doen we met een functie, de afdruk wordt vanuit het hoofdprogramma gedaan, dus de functie geeft de kostprijs terug.

· Aantal dagen kan verschillend zijn, zo kan iemand bvb 1 kinderfiets voor 5 dagen geven en een elektrisch fiets voor 3.

· Functie verhuurfiets(Type,Dagen,Verzekering)

Type · Dagprijs

Kinderfiets € 30

Volwassenfiets € 40

Tandem € 50

Elektrische fiets € 50

Pedelec(45 km), Rijbewijs verplicht € 70

· Indien de gebruiker geen rijbewijs heeft, krijgt hij een elektrische fiets in de plaats pedelec, aan € 50 per dag.

· Indien de gebruiker een Verzekering wenst kan dit. Dit is de dagprijs.

Type Dagprijs

Kinderfiets € 8

Volwassenfiets € 10

Tandem € 10

Elektrische fiets € 15

Pedelec(45 km), Rijbewijs verplicht € 25

· Ook zal er een waarborg aangerekend worden, Dit is een vast bedrag dus niet afhankelijk van het aantal dagen

Type

Kinderfiets € 100

Volwassenfiets € 150

Tandem € 150

Elektrische fiets € 200

Pedelec(45 km), Rijbewijs verplicht € 350

Print in hef hoofd programma de prijzen van verhuur. Als ook de totaal prijs
"""
# Functies
def prijsfiets(t,d,v):
    # steek dagprijzen in variabelen
    # indien geen verzekering
    if v.upper()=='N':
        if t.upper()=='A':
            dagprijs=30
        elif t.upper()=='B':
            dagprijs=40
        elif t.upper()=='C' or t.upper()=='D':
            dagprijs=50
        else:
            dagprijs=70
    # indien verzekering
    else:
        if t.upper()=='A':
            dagprijs=38
        elif t.upper()=='B':
            dagprijs=50
        elif t.upper()=='C':
            dagprijs=60
        elif t.upper()=='D':
            dagprijs=65
        else:
            dagprijs=95
    # waarborg
    if t.upper()=='A':
        waarborg=100
    elif t.upper()=='B' or t.upper()=='C':
        waarborg=150
    elif t.upper()=='D':
        waarborg=200
    else:
        waarborg=350
    return waarborg + dagprijs * d 

# Hoofdprogramma
result=[]
aantal_fietsen=int(input('Hoeveel fietsen wenst u te huren?:\n'))           # vraag aan user hoeveel fietsen hij wil huren
for i in range(aantal_fietsen):                                             # loop voor elke fietsaanvraag
    # beetje tricky maar duidelijker wanneer je het programma runt
    type=input('Welk type fiets wenst u te huren?\nA)Kinderfiets\t30€\nB)Volwassenfiets\t40€\nC)Tandemfiets\t50€\nD)Elektrische fiets\t50€\nE)Pedelec\t70€\nKies A,B,C,D of E\n')
    # check voor zekerheid dat we alleen maar ABCDE hebben
    while type.upper() not in ['A','B','C','D','E']:
        type=input('Gelieve het volgende in te geven: A,B,C,D of E:\n')
    # vervang E door D als bestuurder geen rijbewijs heeft
    if type.upper()=='E':
        rijbewijs=input('Beschik je over een rijbewijs? (J/N):\n')
        if rijbewijs.upper()=='J':
            type='E'
        else:
            print('U kan niet rijden met een Pedelec, Elektrische fiets in de plaats geselecteerd')
            type='D'
    # vraag dagen aan user voor de functie
    dagen=int(input('Hoeveel dagen wenst u gebruik te maken van de huurfiets?\n'))
    # vraag voor verzekering
    verzekering=input('Wenst u een verzekering aan te schaffen? (J/N)\n')
    # double check voor J of N
    while verzekering.upper() not in ['J','N']:
        verzekering=input('gelieve enkel J of N in te geven:\n')
    result.append(prijsfiets(type,dagen,verzekering))

# Output
# resultaat per fiets
for i in range(1,aantal_fietsen+1):
    print('Fiets',i,': \t',result[i-1],'euro')
# resultaat totaalprijs
print('totaalprijs: \t',sum(result),'euro')
