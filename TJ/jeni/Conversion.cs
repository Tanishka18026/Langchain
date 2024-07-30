class Conversion
{
	public static void Main(string[] args)
	{
		decimal a = 75.79M ;
		int result = System.Convert.ToInt32(a * 100);
		System.Console.WriteLine("THE Conversion of FLoat is" +result);
	}
}