def c_na_f(c):
    return (c * 9 / 5) + 32

def f_na_c(f):
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    print("Konwerter temperatury. Wybierz kierunek przemiany:")
    print("Celsjusz -> Fahrenheit = KLIKNIJ C")
    print("Fahrenheit -> Celsjusz = KLIKNIJ F")

    wybor = input().upper()

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