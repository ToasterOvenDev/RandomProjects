public class B
{
   public static void main(String[] args)
   {
      nine();
   }
   
   public static void one()
   {
      int i = 3;
      while (i<8)
      {
         i = i +1;
      }
      System.out.println("i is " + i);
   }
   
   public static void two()
   {
      for(int i = 20; i > 0; i--)
      {
         if(i%2==0)
         {
            System.out.print(i);
         }
      }
   }
   
   public static void three()
   {
      for( int i = 0; i < 20; i++)
      {
          if(i%2==0)
             {
                System.out.print(i*2);
              }
      }
   }
   
   public static void four()
   {
      for( int i = 5; i > 0; i--)
      {
         int num = 100;
         num-=i;
         System.out.print(num);
      }
   }
   
   public static void five()
   {
      int num = 100;
      for( int i = 5; i > 0; i--)
      {
         num -= i;
      }
      System.out.println(num);
   }
   
   public static void six()
   {
      int val = 0;
      int num = 0;
      do
      {
         num++;
         val=val+num;
         if(val>4)
         {
            break;
         }
      }
      while(num<5);
      System.out.print(val);
   }
   
   public static void seven()
   {
      int num = 1;
      int counter = 1;
      while(num<3)
      {
         num=num*counter;
         counter++;
      }
      System.out.println(num);
   }
   
   public static void eight()
   {
      int i = 0;
      while(i < 8)
      {
         System.out.println("whatever");
         i = i + 1;
      }
   }
   
   public static void nine()
   {
      for(int i = 1; i <=10; i++)
      {
         System.out.print(i);
         i++;
      }
   }
}