import java.util.Scanner;

public class AccountTest
{
   public static void main(String[] args)
   {
      Scanner scan = new Scanner(System.in);
      
      System.out.printf("Enter account Holder name:");
      String accountHolder = scan.nextLine();
      System.out.printf("Enter account number:");
      int accountNumber = scan.nextInt();
      System.out.printf("Enter account balance:");
      double balance = scan.nextDouble();
      System.out.printf("%n%n");

      
      Account Account = new Account();
      
      Account.setHolder(accountHolder);
      Account.setNumber(accountNumber);
      Account.setBalance(balance);
      
      System.out.printf("Account Holder:%s%nAccount Number:%d%nBalance:$%,.2f",
      Account.getHolder(),Account.getNumber(),Account.getBalance());
   }
}