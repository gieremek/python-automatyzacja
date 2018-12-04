# Rozdział drugi - sterowanie przepływem
#********** Pobieranie danych *************************
# Prośba o podanie imienia
print('Jak masz na imie?') 
name = input()
# Prośba o podanie wieku
print('Ile masz lat')
age = int(input())  #konwersja na liczbe calkowita

#********* Logika aplikacji **************************
if name == 'Alicja' :
    print('Witaj, Alicja.')
elif age < 12 :
    print('Nie jesteś Alicją, dzieciaku.')
elif age > 100:
    print('Nie jesteś Alicją, dziadku.')
elif age > 2000:
    print('Jestś nieśmiertelnym wampirem.')

