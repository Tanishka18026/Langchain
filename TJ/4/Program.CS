using System;
using System.Math;

class Program
{
    static void Main(string[] args)
    {
        double demandRate = double.Parse(args[0]);
        double setupCost = double.Parse(args[1]);
        double holdingCost = double.Parse(args[2]);
        double EOQ = Math.Sqrt(2 * demandRate * setupCost / holdingCost);
        double PPO = Math.Sqrt(2 * setupCost / (demandRate * holdingCost));
        Console.WriteLine(String.Format("EOQ: {0}", EOQ));
        Console.WriteLine(String.Format("PPO: {0}", PPO));
    }
}