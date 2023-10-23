"""
Casus 1: Willekeurige lijst.

· Vul een lijst met 47 willekeurige getallen tussen 20 en 200.

· De gebruiker geef hierna zelf nog 3 getallen in. Geen invoercontrole nodig

· Druk de 3 grootste getallen uit de lijst af

· Toon het gemiddelde van de lijst.

· Druk de lijst van groot naar klein af.

"""

# modules
import random as r

# hoofdprogramma
result = []                                         # maak lege lijst met 47 entries
for x in range(47):                                 # start loop voor random appends
    result.append(r.randrange(20,200))              # randrange voor 20 - 200 toeveogen aan de lijst

for x in range(3):                                  # start loop voor user appends
    userinput=int(input('geef een getal in: '))     # vraag user voor input
    result.append(userinput)                        # manuele entries toevoegen aan lijst

result.sort()                                       # sorteer van groot naar klein

print('Grootste 3 getallen uit de lijst:\t',result[-3:])                                  # print 3 grootste getallen (3 laatste getallen van lijst)
print('Het gemiddelde van de lijst is: \t',sum(result)/len(result))                       # print het gemiddelde van de lijst af
print('De lijst van groot naar klein:\n',result[::-1])                                    # print lijst van achter naar voor af



    





