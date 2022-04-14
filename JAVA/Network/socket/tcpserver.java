import java.io.*;
import java.net.*;
import java.util.*;
class tcpserver
{
public static void main(String args[]) throws Exception
{
ServerSocket soc=new ServerSocket(10000);
System.out.println("Server is Ready......Waiting for Client Request......");
while(true)
{
Socket so=soc.accept();
OutputStream os=so.getOutputStream();
DataOutputStream dos=new DataOutputStream(os);
Date d=new Date();
dos.writeUTF(d.toString());
dos.close();
soc.close();
so.close();
}}}

