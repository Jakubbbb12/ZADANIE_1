def dodaj(a,b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "błąd 01: Dzielenie przez 0 jest niewykonalne"
    return a / b

if __name__ == "__main__":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print("Wybierz działanie: + - * /")
    operacja = input("Wybrano: ")

    if operacja == "+":
        print("Wynik:", dodaj(a, b))
    elif operacja == "-":
        print("Wynik:", odejmij(a, b))
    elif operacja == "*":
        print("Wynik:", mnoz(a, b))
    elif operacja == "/":
        print("Wynik:", dziel(a, b))
    else:
        print("Nieznana operacja.")