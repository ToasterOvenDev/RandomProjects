import javax.swing.*;

public class LabCourse extends CollegeCourse
{
   public LabCourse(String d, int n, int h) // Constructor
   {
      super(d,n,h); // Pass information to parent class constructor
      super.fee = super.fee + 50; // Add 50 dollars to the fee
   }
   
   public void display() // Override parent display method
   {  
      JOptionPane.showMessageDialog(null, "Warning Course is a Lab, extra $50 Lab Fee added to total"); // Warn about increase price and why
      super.display(); // Display the rest of the information with parent display method
   }
}