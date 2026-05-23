public class TestingB
{
   public static void main(String[] args)
   {
      B firstB = new B();
      B secondB = new B();
      firstB.b = 9;
      secondB.c = 3.2;
      secondB.b= 6;
      firstB.a = "d";
      secondB.a = "ac";
      firstB.c = 1.7;
      System.out.printf("%s%d%.2f",secondB.a + firstB.a,
      3 * secondB.b - 4 *firstB.b, firstB.c - secondB.c);
   }
}