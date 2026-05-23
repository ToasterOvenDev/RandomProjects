import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class JFontUpdate extends JFrame implements ActionListener, MouseListener 
{
   JMenuBar bar = new JMenuBar();
   JMenu fontMenu = new JMenu("Font");
   JMenu colorMenu = new JMenu("Color");
   JMenu extraMenu = new JMenu("Extra");
   JMenu sizeMenu = new JMenu("Size");
   
   int fontSize = 16;
   
   Font comicSans = new Font("Comic Sands MS", Font.PLAIN, fontSize);
   Font timesNR = new Font("Times New Roman", Font.PLAIN, fontSize);
   Font arial = new Font("Arial", Font.PLAIN, fontSize);
   
   JMenuItem cS = new JMenuItem("Comic Sans MS");
   JMenuItem tNR = new JMenuItem("Times New Roman");
   JMenuItem a = new JMenuItem("Arial");
   
   JMenuItem up = new JMenuItem("Font Size Up");
   JMenuItem down = new JMenuItem("Font Size Down");
   
   JMenuItem bolden = new JMenuItem("Bold");
   JMenuItem itali = new JMenuItem("Italics");
   JMenuItem plain = new JMenuItem("Plain");
   
   JRadioButtonMenuItem blue = new JRadioButtonMenuItem("Blue", true);
   JRadioButtonMenuItem gray = new JRadioButtonMenuItem("Gray");
   JRadioButtonMenuItem yellow = new JRadioButtonMenuItem("Yellow");
   
   JLabel welcome = new JLabel("Welcome to Dalton State", JLabel.CENTER);
   JLabel label = new JLabel("Many colors exist here!", JLabel.CENTER);
   ButtonGroup group = new ButtonGroup();
   ButtonGroup group2 = new ButtonGroup();
   ButtonGroup group3 = new ButtonGroup();
   Container con = getContentPane();
   
   public JFontUpdate() {
      con.setLayout(new GridLayout(2,0));
      
      welcome.setFont(new Font("Comic Sans MS", Font.BOLD, 24));
      welcome.setForeground(Color.BLUE);
      label.setFont(arial);
      label.setForeground(Color.BLUE);
      con.add(welcome);
      con.add(label);
      con.setBackground(Color.YELLOW);

      group.add(yellow);
      group.add(blue);
      group.add(gray);
      group2.add(bolden);
      group2.add(itali);
      group2.add(plain);
      group3.add(cS);
      group3.add(tNR);
      group3.add(a);
      
      setJMenuBar(bar);
      bar.add(sizeMenu);
         sizeMenu.add(up);
         sizeMenu.add(down);
      bar.add(fontMenu);
         fontMenu.add(cS);
         fontMenu.add(tNR);
         fontMenu.add(a);
      bar.add(colorMenu);
         colorMenu.add(blue);
         colorMenu.add(gray);
         colorMenu.add(yellow);
      bar.add(extraMenu);
         extraMenu.add(bolden);
         extraMenu.add(itali);
         extraMenu.add(plain);
         
      fontMenu.setMnemonic('F');
      colorMenu.setMnemonic('C');
      extraMenu.setMnemonic('E');
      sizeMenu.setMnemonic('S');
      
      cS.addActionListener(this);
      tNR.addActionListener(this);
      a.addActionListener(this);
      bolden.addActionListener(this);
      itali.addActionListener(this);
      plain.addActionListener(this);
      up.addActionListener(this);
      down.addActionListener(this);
      gray.addActionListener(this);
      blue.addActionListener(this);
      yellow.addActionListener(this);
      addMouseListener(this);
      
      
   }
   
   public void actionPerformed(ActionEvent e) {
      Object source = e.getSource();
      if(source == blue)
         label.setForeground(Color.BLUE);
      else if(source == gray)
         label.setForeground(Color.GRAY);
      else if(source == yellow)
         label.setForeground(Color.YELLOW);
      else if(source == cS)
         label.setFont(comicSans);
      else if(source == tNR)
         label.setFont(timesNR);
      else if(source == a)
         label.setFont(arial);
      else if(source == up)
      {
         fontSize++;
         label.setFont(label.getFont().deriveFont((float)fontSize));
      }
      else if(source == down)
      {
         fontSize--;
         label.setFont(label.getFont().deriveFont((float)fontSize));
      }
      else if(source == bolden)
         label.setFont(label.getFont().deriveFont(Font.BOLD));
      else if(source == itali)
         label.setFont(label.getFont().deriveFont(Font.ITALIC));
      else if(source == plain)
         label.setFont(label.getFont().deriveFont(Font.PLAIN));
   }
   
   public void mouseExited(MouseEvent e) 
   {
      con.setBackground(Color.LIGHT_GRAY);
   }
   public void mouseEntered(MouseEvent e) 
   {
      con.setBackground(Color.YELLOW);
   }
   public void mousePressed(MouseEvent e) {}
   public void mouseReleased(MouseEvent e) {}
   public void mouseClicked(MouseEvent e) {}
   
   public static void main(String [] args) 
   {
      JFontUpdate frame = new JFontUpdate();
      frame.setSize(300,250);
      frame.setVisible(true);
      frame.setLocationRelativeTo(null);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}