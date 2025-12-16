# Deze opdracht komt van lesvoorbereiding hoofdstuk 5

### Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8

getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))
som = getal1 + getal2
print(f'{getal1} + {getal2} = {som}')


### Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12
getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))
product = getal1 * getal2

print(product)

### Geef nu het resultaat weer in een string. waar de getallen en het resultaat in staan.
print(f'{getal1} * {getal2} = {product}')

### Laat python de wortel van een getal berekenen en het resultaat printen
# De wortel van 16 is 4
# Tip gebruik ** om de wortel te berekenen
getal1 = int(input('Voer eerste getal in: '))
wortel = getal1 ** 0.5

print(wortel)



### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1
getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))
rest = getal1 % getal2

print(rest)


### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
# Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

# === MIJN ANTWOORD ===
getal1 = int(input('Voer eerste getal in: '))
getal2 = int(input('Voer tweede getal in: '))

som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
quotient = getal1 / getal2

print(f'{getal1} + {getal2} = {som}')
print(f'{getal1} - {getal2} = {verschil}')
print(f'{getal1} * {getal2} = {product}')
print(f'{getal1} / {getal2} = {quotient}')
