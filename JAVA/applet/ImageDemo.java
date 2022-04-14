import java.applet.Applet; import java.awt.*;
import java.awt.event.*; import java.net.URL;
public class ImageDemo extends java.applet.Applet
{
Image img; public void init()
{
}
public void paint(Graphics g)
{


URL url1 = getCodeBase();
img = getImage(url1,"deva.jpg"); g.drawImage(img, 5,5, this);
}
}