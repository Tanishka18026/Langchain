using System;

class Prac2a2
{   
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter the amount in paise:");
        string input = Console.ReadLine();

        if (float.TryParse(input, out float paise))
        {
            float rupees = paise / 100;
            Console.WriteLine(+paise+ " paise is equal to " +rupees+ " rupees.");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid number.");
        }
    }
}
