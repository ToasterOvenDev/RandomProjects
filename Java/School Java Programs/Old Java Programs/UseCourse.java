import javax.swing.*;

public class UseCourse
{
   public static void main(String [] args)
   {
      CollegeCourse course; // Set up CollegeCourse Variable, don't fill it out yet
      LabCourse lCourse; // Set up LabCourse Variable, don't fill it out yet
      String userinD = JOptionPane.showInputDialog("Department Code?"); // Ask for Department
      int userinCN = Integer.parseInt(JOptionPane.showInputDialog("Course Number?")); // Ask for the Course Number
      int userinCH = Integer.parseInt(JOptionPane.showInputDialog("Course Hours?")); // Ask for the Course Hours
      
      
      
      String[] labCourses = { "BIOL", "CHEM", "CMPS", "PHYS" }; // Set up an array that holds all lab course departments
      boolean lab = false; // Make a boolean so we can check if a lab course department was matched in the array
      
      for(int i = 0; i<labCourses.length; i++) // Loop through the labCourses array and check for a match
      {
         if(labCourses[i].equals(userinD)) // Match is found
         {
            lCourse = new LabCourse(userinD,userinCN,userinCH); // New LabCourse Object filled out
            lCourse.display(); // Use LabCourse.java display method
            lab = true; // Lab course found set boolean to true
            break; // Found a lab course don't need to continue looping
         }
      }
      if(lab == false) // A lab course has not been found
      {
         course = new CollegeCourse(userinD,userinCN,userinCH); // New CollegeCourse Object filled out
         course.display(); // Use CollegeCourse.java display method
      }
   }
}