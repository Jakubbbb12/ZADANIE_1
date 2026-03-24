using System;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Konwerter temperatury. Wybierz kierunek przemiany: ");
        Console.WriteLine("Celsjusz -> Fahrenheit = KLIKNIJ C");
        Console.WriteLine("Fahrenheit -> Celsjusz = KLIKNIJ F");
        string wybor = Console.ReadLine();
        if (wybor == "C")
        {
            Console.Write("Podaj tempetarutę w Celsjuszach: ");
            double celsjusz = double.Parse(Console.ReadLine());
            double fahrenheit = (celsjusz * 1.8) + 32;
            Console.WriteLine($"Wynik: {fahrenheit} °F");
        }
        else if (wybor == "F")
        {
            Console.Write("Podaj tempetarutę w Fahrenheitach: ");
            double fahrenheit = double.Parse(Console.ReadLine());
            double celsjusz = (fahrenheit - 32) / 1.8;
            Console.WriteLine($"Wynik: {celsjusz} °C");
        }
        else
        {
            Console.WriteLine("Nieprawidłowy wybór.");
        }
    }
}