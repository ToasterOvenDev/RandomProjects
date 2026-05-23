public class Account
{
   private String accountHolder;
   private int accountNumber;
   private double balance;
   
   public String getHolder()
   {
      return accountHolder;
   }
   
   public int getNumber()
   {
      return accountNumber;
   }
   
   public double getBalance()
   {
      return balance;
   }
   
   public void setHolder(String accountHolder)
   {
      this.accountHolder = accountHolder;
   }
   
   public void setNumber(int accountNumber)
   {
      this.accountNumber = accountNumber;
   }
   
   public void setBalance(double balance)
   {
      this.balance = balance;
   }
}