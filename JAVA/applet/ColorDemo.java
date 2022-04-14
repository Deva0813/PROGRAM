import java.awt.*;
import java.applet.*;

public class ColorDemo extends Applet { public void init() {
setBackground(Color.CYAN);
}
public void paint(Graphics g) {
g.drawRect(220, 100, 150, 100); 
g.setColor(Color.yellow);
g.fillRect(220,100, 150, 100); 
g.setColor(Color.red);
}
}