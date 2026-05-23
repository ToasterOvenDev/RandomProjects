public class Bill
{
   int number;
   String name;
   double amount;
   
   //Constructors
   public Bill(int number, String name, double amount)
   {
      this.number = number;
      this.name = name;
      this.amount = amount;
   }
   
   public Bill(String name)
   {
      this.name = name;
      number = 999;
      amount = 0.0;
   }
   
   //Calculates tax
   public double calculateTax(double percentage)
   {
      return amount*percentage;
   }
   
   //toString meathod
   @Override
   public String toString()
   {
      return String.format("Name:%s%nNumber:%d%nAmount:$%,.2f",name,number,amount);
   }
   
   //THe Set and Get meathods
   public void setNumber(int number)
   {
      this.number = number;
   }
   
   public int getNumber()
   {
      return number;
   }
  
   public void setName(String name)
   {
      this.name = name;
   }
   
   public String getName()
   {
      return name;
   }
   
   public void setAmount(double amount)
   {
      this.amount = amount;
   }
   
   public double getAmount()
   {
      return amount;
   }
}