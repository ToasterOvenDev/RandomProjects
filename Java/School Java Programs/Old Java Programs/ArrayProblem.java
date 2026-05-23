public class ArrayProblem
{  
   public static void main(String[] args)
   {
      changeFirstCharacter("A","macrotis");
   }
   
   public String changeFirstCharacter(String letter, String word)
   {
      String a = word.substring(0,1);
      return = word.replace(a, letter);
   }
}