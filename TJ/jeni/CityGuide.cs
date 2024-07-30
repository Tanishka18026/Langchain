class CityGuide
{
	public static void Main(string[] args)
	{
		System.Console.WriteLine("select Your Choice");
		System.Console.WriteLine("London");
		System.Console.WriteLine("Bombay");
		System.Console.WriteLine("Paris");
		System.Console.WriteLine("Type Your Choice");
		string name = System.Console.ReadLine();

		switch(name)
		{
			case "Bombay":
		              System.Console.WriteLine("Bombay:Guide 5");
			      break;
			case "London":
			      System.Console.WriteLine("London:Guide 10");
			      break;
			case "Paris":
			      System.Console.WriteLine("Paris:Guide 15");
			      break;
			   default:
			      System.Console.WriteLine("Invalid Choice");
				break;
		}
	}
}