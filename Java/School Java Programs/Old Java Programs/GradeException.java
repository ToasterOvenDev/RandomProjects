public class GradeException extends Exception
{
   public static char [] grades = { 'A','B','C','D','F','I' };
   public GradeException(String msg)
   {
      super(msg);
   }
}