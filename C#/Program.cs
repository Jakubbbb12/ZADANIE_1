using System;
class Program
{
    static void Main(string[] args)
    {
        double a, b, wynik;
        Console.WriteLine("Prosty kalkulator dwóch liczb");
        Console.WriteLine("Podaj liczbę A:");
        a = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Podaj liczbę B:");
        b = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Wybierz działanie: +, -, *, /");
        string operacja = Console.ReadLine();
        switch (operacja)
        {
            case "+":
                wynik = a + b;
                Console.WriteLine("Wynik: " + wynik);
                break;
            case "-":
                wynik = a - b;
                Console.WriteLine("Wynik: " + wynik);
                break;
            case "*":
                wynik = a * b;
                Console.WriteLine("Wynik: " + wynik);
                break;
            case "/":
                if (b != 0)
                {
                    wynik = a / b;
                    Console.WriteLine("Wynik: " + wynik);
                }
                else
                {
                    Console.WriteLine("Nie można dzielić przez zero!");
                }
                break;
            default:
                Console.WriteLine("Nieznana operacja!");
                break;
        }
    }
}