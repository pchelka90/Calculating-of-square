# Prośba o podanie długości prostokąta od użytkownika
dlugosc = float(input("Podaj długość prostokąta: "))

# Prośba o podanie szerokości prostokąta od użytkownika
szerokosc = float(input("Podaj szerokość prostokąta: "))

# Obliczenie pola powierzchni prostokąta
pole_powierzchni = dlugosc * szerokosc

# Wyświetlenie wyniku z dokładnością do 2 miejsc po przecinku
print(f"Pole powierzchni prostokąta wynosi: {pole_powierzchni:.2f}")
