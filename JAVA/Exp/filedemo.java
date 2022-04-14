import java.util.*;
import java.io.*;
class filedemo
{
    public static void main (String agrs[])
{
String filename;
Scanner s=new Scanner(System.in);
System.out.println("Enter the file name:");
filename = s.nextLine();
File fl= new File(filename);
System.out.println("*************************");
System.out.println("FILE INFORMATION");
System.out.println("*************************");
System.out.println("Name of the file: "+fl.getName());
System.out.println("Path of the file: "+fl.getPath());
System.out.println("Parent of file: "+fl.getParent());
if(fl.exists())
{
System.out.println("The file exists");
}
else
{
    System.out.println("The file dones not exists");
}
if(fl.canRead())
{
    System.out.println("The file is readable.");
}
else
{
    System.out.println("The file is not readable..");
}
if(fl.canWrite())
{
    System.out.println("can write the file");
}
else 
{
    System.out.println("Cannot write");
}
}
}