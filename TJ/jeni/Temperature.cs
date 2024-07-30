class Temperature
{
	public static void Main(string[] args)
	{
		float f  = System.Single.Parse(args [0]);
		double C = System.Convert.ToDouble((f - 32)/1.8);
		System.Console.WriteLine(C);
	}
}