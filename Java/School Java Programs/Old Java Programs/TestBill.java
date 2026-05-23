import java.util.Scanner;

public class TestBill
{
   public static void main(String[] args)
   {
      Scanner scan = new Scanner(System.in);
      Bill bill1 = new Bill("Bobby");
      Bill bill2 = new Bill(1023,"Garry",30.0);
      
      System.out.println(bill1);
      System.out.println();
      System.out.println(bill2);
      System.out.println();
      
      System.out.printf("Please enter a percentage for tax: ");
      double tax = scan.nextDouble();
      System.out.printf("The tax for bill 1 is %.2f%n",bill1.calculateTax(tax / 100));
      System.out.printf("The tax for bill 2 is %.2f",bill2.calculateTax(tax / 100));
   }
}