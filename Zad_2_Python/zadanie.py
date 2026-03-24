def c_na_f(c): #przemiana z celsjuszy na fahrenheit
    return (c * 1.8) + 32

def f_na_c(f): #przemiana z fahrenheita na celsjusze
    return (f - 32) * 1.8


if __name__ == "__main__":
    print("Konwerter temperatury. Wybierz kierunek przemiany:")
    print("Celsjusz -> Fahrenheit = KLIKNIJ C")
    print("Fahrenheit -> Celsjusz = KLIKNIJ F")

    wybor = input().upper() 
    #funkcja upper sprawia, ze niezaleznie czy uzytkownik wpisze małą/wielką literą wybór, program zamieni znak na wielki

    if wybor == "C":
        celsjusz = float(input("Podaj temperaturę w Celsjuszach: "))
        fahrenheit = c_na_f(celsjusz)
        print(f"Wynik: {fahrenheit}°F")
    elif wybor == "F":
        fahrenheit = float(input("Podaj temperaturę w Fahrenheitach: "))
        celsjusz = f_na_c(fahrenheit)
        print(f"Wynik: {celsjusz}°C")
    else:
        print("Nieprawidłowy wybór.")