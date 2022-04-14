import java.io.*;
import java.net.*;
class tcpclient
{
public static void main(String args[])throws Exception
{
try
{
Socket ss=new Socket(args[0],10000);
InputStream is=ss.getInputStream();
DataInputStream dis=new DataInputStream(is);
String info=dis.readUTF();
System.out.println("Message From Server");
System.out.println("Received at Client");
System.out.println("\t\t"+info);
dis.close();
ss.close();
}
catch(Exception e)
{
System.out.println("Inside Exception");
}}}