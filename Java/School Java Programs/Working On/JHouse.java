import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;

public class JHouse extends JFrame implements MouseListener
{
   Container con = getContentPane();
   boolean day = true;
   double doubleDarkValue = 255*0.5;
   int darkValue = (int)doubleDarkValue;
   Color houseColorD = new Color(255,0,0);
   Color houseColorN = new Color(darkValue,0,0);
   Color garageColorD = new Color(0,0,255);
   Color garageColorN = new Color(0,0,darkValue);
   Color carColor = new Color(165, 0, 168);
   
   public JHouse()
   {
      super("Lovely House");
      con.setLayout(new FlowLayout());
      addMouseListener(this);
   }
   
   public void paint(Graphics g)
   {
      super.paint(g);
      if(day)
      {
         paintDay(g);
      }
      else
      {
         paintNight(g);
      }
   }
   
   public static void main(String [] args)
   {
      JHouse frame = new JHouse();
      frame.setVisible(true);
      frame.setSize(800,500);
      frame.setDefaultCloseOperation(3);
      frame.setLocationRelativeTo(null);
   }
   
   public void mouseExited(MouseEvent e) // when the mouse is ouside the frame change it to night
   {
      day = false;
      repaint();
   }
   public void mouseEntered(MouseEvent e) // when the mouse is inside the frame change it to day
   {
      day = true;
      repaint();
   }
   public void mousePressed(MouseEvent e) {}
   public void mouseReleased(MouseEvent e) {}
   public void mouseClicked(MouseEvent e) // When the frame is clicked we randomize the color of the house, garage and car
   {
      for(int i=0;i<3;i++)
      {
         double dr; // Double version to prevent lossy conversion
         double dg;
         double db;
         int r = (int)(Math.random()*256); // Random color
         int g = (int)(Math.random()*256);
         int b = (int)(Math.random()*256);
         if(i == 0) // first change the house
            houseColorD = new Color(r,g,b);
         else if(i==1) // then the garage
            garageColorD = new Color(r,g,b);
         else // finally the car
            carColor = new Color(r,g,b);
         dr = r*0.5; // 50% darker
         dg = g*0.5;
         db = b*0.5;
         r = (int)dr; // convert to int
         g = (int)dg;
         b = (int)db;
         if(i == 0) // Do nighttime version
            houseColorN = new Color(r,g,b);
         else if(i==1) // Do nighttime version
            garageColorN = new Color(r,g,b);
      }
      repaint(); // repaint to update colors
   }
   
   public void drawWindow(Graphics g,int x,int y,int w,int h, Color c)
   {
      int midX = x+(w/2); // Find the middle of the x
      int midY = y+(h/2); // Find the middle of the y
      g.setColor(c);
      g.fillRect(x,y,w,h); // Draw the window
      g.setColor(Color.black);
      g.drawLine(midX,y,midX,y+h); // Draw the line down the middle top to bottom
      g.drawLine(x,midY,x+w,midY); // Draw the line down the middle left to right
   }
   public void drawRoof(Graphics g, int srtX,int srtY,int endX,int endY)
   {
      int midX = (endX-srtX)/2;
      midX+=srtX;
      //Outline first in color set before called method
      g.drawLine(srtX,srtY,midX,endY);
      g.drawLine(endX,srtY,midX,endY);
      // Set color to black
      g.setColor(Color.black);
      //Pos of triangle polygon
      int [] mainTriangleX = {srtX,midX,endX,srtX};
      int [] mainTriangleY = {srtY,endY,srtY,srtY};
      g.fillPolygon(mainTriangleX,mainTriangleY,mainTriangleX.length);
      // Decor Lines
      int y = srtY; // start Y is equal to the y we start drawing lines across at
      int x1 = srtX; // X1 srarts at the first point as well
      int x2 = endX; // end X is directly across from the first point
      double slope = (double)(y-endY)/(x1-midX); // Slope of the roof
      double b = y-(slope*x1); // Y-intercept of the roof
      double x; // X variable for later
      int diffXs; // Difference of X1 and the first X point
      g.setColor(Color.gray);
      while( y>endY) // Draw until the Y is at the top
      {
         y-=10; // Every 10 pixels draw a line
         x = (y-b)/slope; // find the X coordanate to start at
         x1 = (int)x; // set it as X1
         diffXs = Math.abs(x1-srtX); // Find the absolute value difference between where we are now and where we started
         x2 = endX-diffXs; // apply the difference to the other side since it's an easier calculation
         g.drawLine(x1,y,x2,y); // Draw the line
      }
   }
   public void drawGarageDoor(Graphics g, int x, int y, int w,int h)
   {
      g.fillRect(x,y,w,h);
      int cY = y+h;
      int eX = x+w;
      g.setColor(Color.black);
      while(cY > y)
      {
         g.drawLine(x,cY,eX,cY);
         cY-=10;
      }
      drawWindow(g,x+20,y+10,w-40,20,Color.blue);
   }
   public void drawCar(Graphics g, int x, int y, Color c)
   {
      g.setColor(Color.gray);
      g.fillOval(x+5,y+5,10,10); // Antenna
      g.drawLine(x+10,y+15,x+10,y+35);
      g.setColor(c);
      g.fillRect(x+5,y+35,100,50); // Main body
      g.fillRect(x+20,y+5,70,30); // Top body
      g.setColor(Color.blue);
      g.fillRect(x+25,y+10,60,20); // Window
      g.setColor(Color.white);
      g.drawLine(x+30,y+30,x+50,y+10); // Window glint
      g.drawLine(x+40,y+30,x+60,y+10); // Window glint
      g.setColor(Color.yellow);
      g.fillOval(x+15,y+50,25,25); // Headlight
      g.fillOval(x+65,y+50,25,25); // Headlight
      g.setColor(Color.black);
      g.fillRect(x+5,y+85,10,20); // Tire
      g.fillRect(x+95,y+85,10,20); // Tire
   }
   public void drawStars(Graphics g)
   {
      int x;
      int y;
      for(int i = 0; i<200; i++)
      {
         x = (int)(Math.random()*800);
         y = (int)(Math.random()*350);
         g.fillOval(x,y,1,1);
      }
   }
   public void paintDay(Graphics g)
   {
      Graphics2D g2d = (Graphics2D)g;
      g2d.setStroke(new BasicStroke(1.0f, BasicStroke.CAP_BUTT,BasicStroke.JOIN_ROUND));
      
      //Background
      g.setColor(new Color(135, 206, 235)); // sky color
      g.fillRect(0,0,800,500); // Sky
      g.setColor(Color.yellow); // Sun color
      g.fillOval(10,35,100,100); // Sun
      g.setColor(Color.green); // Grass Color
      g.fillRect(0,350,800,500); // Grass
      g.setColor(Color.gray); // Driveway Color
      g.fillRect(510,350,130,150); // Driveway
      
      //Main House
      g.setColor(houseColorD); //Main Body Color
      g.fillRect(200,150,300,200); // Main body
      g.setColor(Color.black); // Roof color
      drawRoof(g,200,150,500,50); // Main body Roof
      // Garage
      g.setColor(garageColorD); // Garage Color
      g.fillRect(500,200,150,150); // Garage body
      g.setColor(Color.black); // Garage Roof Color
      drawRoof(g,500,200,650,170);// Garage Roof
      g.setColor(Color.lightGray); // Garage Door Color
      drawGarageDoor(g,510,210,130,140); // Garage door
      
      //House Detail
      g.setColor(new Color(105, 46, 14)); // Porch Color
      g.fillRect(200,345,300,5); // Porch base
      
      g.setColor(new Color(207, 192, 29)); // Door Color
      g.fillRect(220,305,30,40); // Door
      Color windowColor = Color.blue; // Window Color for all windows
      drawWindow(g,225,310,20,10,windowColor); // Door Window
      
      drawWindow(g,295,290,110,35,windowColor);
      drawRoof(g,295,290,405,280);
      drawWindow(g,220,200,75,35,windowColor);
      drawWindow(g,405,200,75,35,windowColor);
      drawWindow(g,338,85,25,25,windowColor);
      // Draw fence
      g.setColor(new Color(105, 46, 14)); // Fence Color
      g2d.setStroke(new BasicStroke(3.0f, BasicStroke.CAP_BUTT,BasicStroke.JOIN_ROUND));
      g2d.draw(new Line2D.Double(200, 325, 440, 325));
      g2d.setStroke(new BasicStroke(3.0f, BasicStroke.CAP_ROUND,BasicStroke.JOIN_ROUND));
      g2d.draw(new Line2D.Double(440, 325, 450, 325));
      int fenceX = 220;
      while(fenceX<=450)
      {
         g2d.draw(new Line2D.Double(fenceX, 325, fenceX, 345));
         fenceX+=20;
      }
   }
   public void paintNight(Graphics g)
   {
      Graphics2D g2d = (Graphics2D)g;
      g2d.setStroke(new BasicStroke(1.0f, BasicStroke.CAP_BUTT,BasicStroke.JOIN_ROUND));
      
      //Background
      g.setColor(Color.black);
      g.fillRect(0,0,800,500); // Sky
      g.setColor(Color.white);
      drawStars(g);
      g.fillOval(10,35,100,100); // Moon
      g.setColor(Color.gray);
      g.fillOval(30,50,20,20);
      g.fillOval(75,60,30,30);
      g.fillOval(25,90,40,40);
      g.setColor(new Color(6,64,14));
      g.fillRect(0,350,800,500); // Grass
      g.setColor(new Color(56, 59, 56));
      g.fillRect(510,350,130,150); // Driveway
      
      //Main House
      g.setColor(houseColorN);
      g.fillRect(200,150,300,200); // Main body
      g.setColor(Color.white);
      g.drawRect(200,150,300,200);// Outline to make more obvious
      drawRoof(g,200,150,500,50); // Main body Roof
      // Garage
      g.setColor(garageColorN);
      g.fillRect(500,200,150,150); // Garage body
      g.setColor(Color.white);
      g.drawRect(500,200,150,150); // Outline to make more obvious
      drawRoof(g,500,200,650,170);// Garage Roof
      g.setColor(Color.black);
      g.fillRect(510,210,130,140);
      drawCar(g,520,250,carColor); // Draw the car
      
      //House Detail
      g.setColor(new Color(79, 38, 15));
      g.fillRect(200,345,300,5); // Porch base
      
      g.setColor(new Color(166, 154, 23));
      g.fillRect(220,305,30,40); // Door
      Color windowColor = new Color(255, 245, 0);
      drawWindow(g,225,310,20,10,windowColor); // Door Window
      
      drawWindow(g,295,290,110,35,windowColor);
      drawRoof(g,295,290,405,280);
      drawWindow(g,220,200,75,35,windowColor);
      drawWindow(g,405,200,75,35,windowColor);
      drawWindow(g,338,85,25,25,windowColor);
      
      //Dude in the window
      g.setColor(Color.black);
      g.fillOval(305,290,20,20);
      g2d.setStroke(new BasicStroke(3.0f, BasicStroke.CAP_BUTT,BasicStroke.JOIN_ROUND));
      g2d.draw(new Line2D.Double(315,310,315,325));
      
      // Fence
      g.setColor(new Color(79, 38, 15));
      g2d.draw(new Line2D.Double(200, 325, 440, 325));
      g2d.setStroke(new BasicStroke(3.0f, BasicStroke.CAP_ROUND,BasicStroke.JOIN_ROUND));
      g2d.draw(new Line2D.Double(440, 325, 450, 325));
      int fenceX = 220;
      while(fenceX<=450)
      {
         g2d.draw(new Line2D.Double(fenceX, 325, fenceX, 345));
         fenceX+=20;
      }
   }
}