using System;
class Program
{
    static void Main(string[] args)
    {
        Console.Write("Podaj liczbę ocen: ");
        int liczba_ocen = int.Parse(Console.ReadLine());

        double suma = 0;

        for (int i = 1; i <= liczba_ocen; i++) //wpisywanie ocen dopóki ich ilość nie wyniesie podanej wcześniej liczbie ocen
        {
            Console.Write($"Podaj ocenę {i}: ");
            double ocena = double.Parse(Console.ReadLine());

            while (ocena < 1 || ocena > 6) //oceny muszą mieścić się w skali
            {
                Console.Write("Ocena jest poza skalą (1-6). Podaj ponownie: ");
                ocena = double.Parse(Console.ReadLine());
            }

            suma += ocena;
        }

        double srednia = suma / liczba_ocen;
        Console.WriteLine($"\nŚrednia ocen: {srednia:F2}"); //wyświetlanie liczby do 2 miejsc po przecinku

        if (srednia >= 3.0)
        {
            Console.WriteLine("Uczeń ZALICZYŁ przedmiot.");
        }
        else
        {
            Console.WriteLine("Uczeń NIE ZALICZYŁ przedmiotu.");
        }
    }
}