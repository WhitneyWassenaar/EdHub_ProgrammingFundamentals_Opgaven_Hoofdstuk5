# Deze opdracht komt uit de EdHub Hoofdstuk 5 > opgaven
# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# ==========================================
from operator import indexOf

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes. Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================


getal_1 = int(input("voer een getal in: "))
getal_2 = int(input("voer een getal in: "))

if getal_1 % getal_2 == 0:
    print(f'{getal_1} is een veelvoud van {getal_2}')
elif getal_2 % getal_1 == 0:
    print(f'{getal_2} is een veelvoud van {getal_1}')
else:
    print(f'Zowel {getal_1} als {getal_2} zijn geen veelvoud van elkaar')

# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================

leeftijd = int(input("voer je leeftijd in: "))
kaartje = 12.00

if 5 > leeftijd >= 0:
    print(f'Jij bent een kind van {leeftijd} jaar. Toegang is gratis!')
elif 12 >= leeftijd >= 5:
    kaartje = kaartje / 2
    print(f'Jij bent een kind van {leeftijd} jaar. Jij betaald de halve prijs, en dat is dus €{kaartje:.2f}.')
elif 54 >= leeftijd >=13:
    print(f'Jij bent {leeftijd} jaar. Jij betaald gewoon de volle prijs van €{kaartje}.')
else:
    print(f'U bent {leeftijd} jaar. U heeft gratis toegang ')


# === UITWERKING ===
# De uitwerking klopt niet! Als je 12 of 54 invoert dan wordt de prijs 0! Dus dit is niet logisch
leeftijd = int(input("voer je leeftijd in: "))
prijs = 12
if leeftijd < 5:
    prijs = 0
elif 5 <= leeftijd < 12:
    prijs = prijs / 2
elif 13 <= leeftijd < 54:
    prijs = prijs
else:
    prijs = 0


print(f"Voor de leeftijd {leeftijd} jaar is de prijs: {prijs}")



# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan). Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3

#num1 = laag   2
#num2 = middel 1
#num3 = hoog 3
# ==========================================
# === MIJN ANTWOORD ===
# Ik begreep maar niet waarom de output niet in de juiste volgorde gesorteerd was.
num1 = int(input("voer getal 1 in: "))
num2 = int(input("voer getal 2 in: "))
num3 = int(input("voer getal 3 in: "))

if num1 > num2:
    num1, num2 = num2, num1
elif num2 > num3:
    num2, num3 = num3, num2
elif num1 > num3:
    num1, num3 = num3, num1

print(num1,num2,num3)

# === JUISTE ANTWOORD ===
#Als je elif in je if-statement hebt, en je hebt bijvoorbeeld 3 x elif, dan zal alleen de eerste elif uitgevoerd worden als dat waar is en de rest wordt dan niet meer uitgevoerd.

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num3:
    num1, num3 = num3, num1

print(num1,num2,num3)



# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0. Schrijf een programma dat herhaaldelijk een getal als input vraagt. Elk getal dat je invoert moet moet worden opgeteld bij het totaal. Als je 0 invoert moet het programma stoppen en met een print statement het totaal en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs). Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================
totaal = 0
aantal_inputs = 0
invoer = int(input('Voer getal in: '))

while invoer != 0:
    totaal += invoer
    aantal_inputs += 1
    invoer = int(input('Voer getal in: '))

# De if/else statement staat buiten de while loop.
if aantal_inputs != 0:
    gemiddelde = totaal / aantal_inputs
    print(f'Het totaal is {totaal} en het gemiddelde is {gemiddelde}')
else:
    print('Er zijn geen getallen ingevoerd')


# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================

# === MIJN ANTWOORD ===
# Helemaal fout, maar ik dacht dat je 'range' kon gebruiken. Daar blijf ik dus volgende keer van af. En i staat dus voor het aantal in range. Dus als rage(1,11) is zal i 1 t/m 10 keer geprint worden.
factor = int(input('Voer heel getal in'))

for factor in range(1,11):
    result = factor * range
    print(f'{range} X {factor} = {result}')

# === JUISTE ANTWOORD ===
factor = int(input('Voer heel getal in: '))

for i in range(1,11):
    result = i * factor
    print(f'{i} X {factor} = {result}')








