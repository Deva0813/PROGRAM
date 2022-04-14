import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
public class FontDemo extends java.applet.Applet
 {
 Font f;
 String m;
 public void init()
 {
 f=new Font("Arial",Font.ITALIC,20);
 m="Welcome to Java";
 setFont(f);
 }
 public void paint(Graphics g)
 {
 Color c=new Color(100,100,255);
 g.setColor(c);
 g.drawString(m,4,20);
Font plainFont = new Font("Serif", Font.PLAIN, 24);
 g.setFont(plainFont);
 g.drawString("Font in PLAIN", 50, 70);
 Font italicFont = new Font("Serif", Font.ITALIC, 24);
 g.setFont(italicFont);
 g.drawString("Font in ITALIC", 50, 120);
 Font boldFont = new Font("Serif", Font.BOLD, 24);
 g.setFont(boldFont);
 g.drawString("Font in BOLD", 50, 170);
 Font boldItalicFont = new Font("Serif", Font.BOLD+Font.ITALIC, 24);
 g.setFont(boldItalicFont);
 g.drawString("Font in BOLD ITALIC", 50, 220);
 }
 } 