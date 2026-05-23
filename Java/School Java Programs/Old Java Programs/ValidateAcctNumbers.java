import java.nio.file.*;
import java.io.*;
public class ValidateAcctNumbers
{
   public static void main(String [] args) throws IOException
   {
      Path file = Paths.get("AcctNumbers.txt");
      InputStream input = null;
      String acct = "";
      int acctNum, lastDigit, digit, sum;
      
      try
      {
         input = Files.newInputStream(file);
         BufferedReader reader = new BufferedReader(new InputStreamReader(input));
         acct = reader.readLine();
         while(acct != null)
         {
            sum = 0;
            acctNum = Integer.parseInt(acct);
            lastDigit = acctNum % 10;
            acctNum /=10;
            
            for(int i = 0; i< acct.length(); i++)
            {
               digit = acctNum % 10;
               sum += digit;
               acctNum /=10;
            }
            
            sum %= 10;
            if(acct.length() != 6)
               System.out.println("Account " + acct + " is invalid length");
            else if(sum == lastDigit)
               System.out.println("The account " + acct + " is valid");
            else
               System.out.println("The account " + acct + " is not valid");
               
            acct = reader.readLine();
         }
         input.close();
      }
      catch(IOException e)
      {
         System.out.println(e);
      }
      catch(NumberFormatException e)
      {
         System.out.println(acct + " not an integer");
      }
      catch(Exception e)
      {
         System.out.println("Something went wrong!");
      }
   }
}