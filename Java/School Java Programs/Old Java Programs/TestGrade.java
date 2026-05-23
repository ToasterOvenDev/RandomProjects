import java.util.*;
public class TestGrade
{
   public static int [] studentIDs = { 9001,9002,9003,9004,9005,9006,9007,9008,9009,9010 };
   public static char [] studentGrades = new char[10];
   
   public static void main(String [] args)
   {
      Scanner scan = new Scanner(System.in);
      char grade;  
      String msg = "Student ID | Grade\n";
      for(int i = 0; i<studentIDs.length; i++)
      {
         boolean gradeAccpt = false;
            try
            {
               System.out.print("Enter student " + studentIDs[i] + " grade: ");
               grade = scan.next().charAt(0);
               boolean good = false;
               for(int j = 0; j<GradeException.grades.length; j++)
               {
                  if(grade == GradeException.grades[j])
                  {
                     msg += "   " + studentIDs[i] + "    |   " + GradeException.grades[j] + "\n";
                     good = true;
                  }
               }
               if(!good)
               {
                  throw new GradeException("Grade not accepted");
               }
            }
            catch(GradeException e)
            {
               msg += "   " + studentIDs[i] + "    |   " + GradeException.grades[5] + "\n";
               System.out.println("You entered an invalid grade, I will represent grade instead!");
            }
            catch(Exception e)
            {
               System.out.println("Something went wrong!");
               e.printStackTrace();
            }
      }
      System.out.println("\n\n" + msg);
   }
}