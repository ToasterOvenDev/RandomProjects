public class TestGrid
{
   public static void main(String [] args)
   {
      GridMap map = new GridMap(30,30);
      int [] pos = {3,5};
      int [] pos2 = {10,7};
      int [] pos3 = {14,14};
      map.placeCharacter(pos);
      boolean test = map.checkSpace(pos);
      System.out.println(test);
      try
      {   
         map.forceSpacesEmpty(pos3,pos2);
      }
      catch(Exception e)
      {
         System.out.println(e.getMessage());
      }
      test = map.checkSpace(pos);
      System.out.print(test);
   }
}