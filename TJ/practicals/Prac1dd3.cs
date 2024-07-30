using System;

class Prac1dd3
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            System.Console.WriteLine("Please provide a character as a command line argument.");
            return;
        }

        char ch = args[0][0];

        if (IsVowel(ch))
        {
            System.Console.WriteLine(Convert.ToString(ch) + " is a vowel.");
        }
        else
        {
            System.Console.WriteLine(Convert.ToString(ch) + " is not a vowel.");
        }
    }

    static bool IsVowel(char ch)
    {
        ch = char.ToLower(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
