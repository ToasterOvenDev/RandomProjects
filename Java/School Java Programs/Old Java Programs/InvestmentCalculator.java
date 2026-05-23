public class InvestmentCalculator
{
   public static void main(String[] args)
   {
   double present = 123.45;
   double rate = 0.025;
   double compounded = 4;
   double time = 12;
   double investment = present*Math.pow(1+rate/compounded, compounded*time);
   System.out.println("If " + present + " is invested at an annual interest rate of " + rate + ", compounded 4 times a year for " + compounded +
    " times each year for " + time + " years, the future value is " + investment);
   }
}
