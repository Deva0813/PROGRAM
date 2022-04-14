import java.awt.*; import java.applet.*;

public class ShapesDemo extends Applet 
{ 
	public void init() {}
	public void paint(Graphics g) 
{ 
	Graphics2D g2d = (Graphics2D)g; 
 		g2d.setColor(Color.blue);
 		g2d.drawRect(75,75,300,200);
	Font exFont = new Font("TimesRoman",Font.PLAIN,40);
 		g2d.setFont(exFont);
 		g2d.setColor(Color.black); 
 		g2d.drawString("Graphics2D Example",120.0f,100.0f); 
 		g2d.setColor(Color.green);
 		g2d.drawLine(100,100,300,200);
 		g2d.drawOval(150,150,100,200);
 		g2d.fillOval(150,150,100,200);
}
}