class StraightLine
{
	public static void Main(string[] args)
	{
	int salvagevalue;
	int purchase_price = System.Convert.ToInt32(args[0]);
	int years_service = System.Convert.ToInt32(args[1]);
	int Annual_Descrip = System.Convert.ToInt32(args[2]);
 	salvagevalue = purchase_price - Annual_Descrip;
	Annual_Descrip = purchase_price - salvagevalue/years_service;
	//salvagevalue = purchase_price - Annual_Descrip;
	//System.Console.WriteLine("The Annual Descrip is "+Annual_Descrip);
	System.Console.WriteLine("The Salvage value is "+ salvagevalue);
	}
}