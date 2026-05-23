import javax.swing.*;
import java.awt.*;

public class JDiagonalLines extends JFrame
{
   Container con = getContentPane();
   
   public JDiagonalLines() {
      con.setLayout(new FlowLayout());
   }
   
   public void paint(Graphics g) {
      super.paint(g);
      final int INCREASE = 20;
      int x = 50;
      int y = 50;
      g.drawRect(x,y,300,300);
      
      
      while(x<350)
      {
         g.drawLine(50,y,x,50);
         x+=INCREASE;
         y+=INCREASE;
      }
      x = 50;
      y = 50;
      while(y<350)
      {
         g.drawLine(350,y,x,350);
         x+=INCREASE;
         y+=INCREASE;
      }
   }
   
   public static void main(String [] args) {
      JDiagonalLines frame = new JDiagonalLines();
      frame.setSize(400,400);
      frame.setVisible(true);
      frame.setLocationRelativeTo(null);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}