public class A
{
   private String a;
   private int b;
   private double c;
   
   public String getA()
   {
      System.out.print(1);
      return a;
   }
   
   public void setA(String a)
   {
      System.out.print(2);
      this.a = a;
   }
   
   public int getB()
   {
      System.out.print(3);
      return b;
   }
   
   public void setB(int b)
   {
      System.out.print(4);
      this.b = b;
   }
   
   public double getC()
   {
      System.out.print(5);
      return c;
   }
   
   public  void setC(double c)
   {
      System.out.print(6);
      this.c = c;
   }
}