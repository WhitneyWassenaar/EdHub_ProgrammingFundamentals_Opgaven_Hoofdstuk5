# Deze opdracht komt van lesvoorbereiding hoofdstuk 5

# geef 2 getallen op en kijk of ze gelijk zijn
# 5 en 5 zijn gelijk
# 5 en 3 zijn niet gelijk

getal_1 = int(input('Voer eerste gehele getal in: '))
getal_2 = int(input('Voer tweede gehele getal in: '))

if getal_1 == getal_2:
    print(f'{getal_1} en {getal_2} zijn gelijk')
else:
    print(f'{getal_1} en {getal_2} zijn niet gelijk')


# geef 2 getallen op en kijk of getal1 groter is dan getal2
# 5 is groter dan 3
# 3 is niet groter dan 5

getal_1 = int(input('Voer eerste gehele getal in: '))
getal_2 = int(input('Voer tweede gehele getal in: '))

if getal_1 > getal_2:
    print(f'{getal_1} is groter dan {getal_2}')
else:
    print(f'{getal_1} is kleiner dan {getal_2}')




# geef 2 getallen op en kijk of getal1 kleiner is dan getal2 of gelijk aan getal2
# 5 is kleiner dan 3
# 3 is kleiner dan 5
# 5 is niet kleiner dan 5

# === MIJN ANTWOORD ===
# Ik vond het logischer om 'groter dan' aan te geven in plaats van 'niet kleiner dan'
getal_1 = int(input('Voer eerste gehele getal in: '))
getal_2 = int(input('Voer tweede gehele getal in: '))

if getal_1 < getal_2:
    print(f'{getal_1} is kleiner dan {getal_2}')
elif getal_2 < getal_1:
    print(f'{getal_1} is groter dan {getal_2}')
else:
    print(f'{getal_1} is gelijk aan {getal_2}')

# === UITWERKING ===
# Hier werd er met 3 getallen gewerkt om meerdere scenario's te laten zien.
getal1 = 5
getal2 = 5
getal3 = 3
print(f"{getal1} is kleiner dan of gelijk aan {getal3} : {getal1 < getal3}")
print(f"{getal3} is kleiner dan of gelijk aan {getal1} : {getal3 < getal1}")
print(f"{getal1} is kleiner dan of gelijk aan {getal2} : {getal1 <= getal2}")

# Kijk of een string gelijk is aan een andere string
# John is gelijk aan John
# John is niet gelijk aan Doeg

# === MIJN ANTWOORD ===
# Ik heb het voorbeeld genomen van de vorige uitwerking. Je kan dus een conditie tussen curly brackets plaatsen om te kijken of het True of False is.
john = "John"
doeg = "Doeg"
print(f'{john} is gelijk aan {john} : {john == john}')
print(f'{john} is niet gelijk aan {doeg} : {john != john}')

