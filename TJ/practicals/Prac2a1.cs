class Prac2a1
{
    static void Main()
    {
        System.Console.Write("Enter a number: ");
        int number = int.Parse(System.Console.ReadLine());

        if (number < 0)
        {
            System.Console.WriteLine("Number must be non-negative.");
            return;
        }

        long factorial = 1;

        for (int i = 2; i <= number; i++)
        {
            factorial *= i;
        }

        System.Console.WriteLine("The factorial of " + number + " is " + factorial);
    }
}