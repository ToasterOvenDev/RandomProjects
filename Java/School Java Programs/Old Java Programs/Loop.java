import java.util.Scanner;

public class Loop
{
   public static void main(String[] args)
   {
      Scanner scan = new Scanner(System.in);
      String word = "";
      String total = "";
      while(true)
      {
         System.out.printf("Enter a word or enter \"halt\" to quit: ");
         word = scan.nextLine();
         
         if(word.equals("halt"))
         {
            break;
         }
         
         total = total + word;
      }
      System.out.println(total);
   }
}