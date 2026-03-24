def pobierz_ocene(numer): #funkcja do pobierania ocen zgodnie ze skalą
    while True:
        ocena = float(input(f"Podaj ocenę {numer}: "))
        if 1 <= ocena <= 6:
            return ocena
        else:
            print("Ocena wykracza poza skalę.")


if __name__ == "__main__":
    liczba_ocen = int(input("Podaj liczbę ocen: "))

    suma = 0

    for i in range(1, liczba_ocen + 1): #podawanie ocen do momentu, gdy ich ilość wyniesie wcześniej podaną liczbę ocen
        ocena = pobierz_ocene(i)
        suma += ocena

    srednia = suma / liczba_ocen
    print(f"\nŚrednia ocen: {srednia:.2f}") #wyświetlanie liczby do 2 miejsc po przecinku

    if srednia >= 3.0:
        print("Uczeń ZALICZYŁ przedmiot.")
    else:
        print("Uczeń NIE ZALICZYŁ przedmiotu.")