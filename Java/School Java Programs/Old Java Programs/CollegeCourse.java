import javax.swing.*;

public class CollegeCourse
{
   // Variables
   protected String department;
   protected int courseNum;
   protected int creditHours;
   protected double fee;
   
   public CollegeCourse(String d, int n, int h) // Constructor
   {
      // Set the variables with passed parameters
      department = d;
      courseNum = n;
      creditHours = h;
      
      // Calculate the fee for the course
      fee = calculateFee();
   }
   
   private double calculateFee() // Private caclulate fee since only CollegeCourse needs the method
   {
      return 120*creditHours;
   }
   
   public void display() // Display the information calculated along with passed information
   {
      JOptionPane.showMessageDialog(null, String.format("Department:%s %nCourse Number:%d %nCredit Hours:%d %nTotal Billed:$%.2f",department,courseNum,creditHours,fee));
   }
}