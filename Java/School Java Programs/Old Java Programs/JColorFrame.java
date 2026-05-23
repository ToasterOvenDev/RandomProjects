import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class JColorFrame extends JFrame implements ActionListener
{
   //Variable
   JPanel p1 = new JPanel();
   JPanel p2 = new JPanel();
   JPanel p3 = new JPanel();
   JPanel p4 = new JPanel();
   JButton colorButton = new JButton("Change Color");
   Container con = getContentPane();
   int index = 0;
   
   
   //Constructor
   public JColorFrame()
   {
      super("JColorFrame");
      con.setLayout(new BorderLayout());
      con.add(p1, "North");
      con.add(p2, "East");
      con.add(p3, "South");
      con.add(p4, "West");
      con.add(colorButton, "Center");
      
      colorButton.addActionListener(this);
      
   }
   //ActionListers
   public void actionPerformed(ActionEvent e)
   {
      int r = (int)(Math.random()*256);
      int g = (int)(Math.random()*256);
      int b = (int)(Math.random()*256);
      Color color = new Color(r,g,b);
      
      if(index == 0)
      {
         changeColor(p1,color);
         index++;
      }
      else if(index == 1)
      {
         changeColor(p2,color);
         index++;
      }
      else if(index == 2)
      {
         changeColor(p3,color);
         index++;
      }
      else
      {
         index = 0;
         changeColor(p4,color);
      }
      
   }
   //Main Method
   public static void main(String [] args)
   {
      JColorFrame frame = new JColorFrame();
      frame.setSize(300,250);
      frame.setLocationRelativeTo(null);
      frame.setDefaultCloseOperation(3);
      frame.setVisible(true);
   }
   
   public void changeColor(JPanel panel, Color color)
   {
      panel.setBackground(color);
   }
}