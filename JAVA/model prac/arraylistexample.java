import java.util.*;
import java.io.*;
public class arraylistexample 
{
  public static void main(String arg[])throws IOException
  { 
    ArrayList<String> obj=new ArrayList<String>();
    DataInputStream in=new DataInputStream(System.in);
      int c,ch;
      int i,j;
      String str,str1;
      do
      {
      System.out.println("String Manipulation");
      System.out.println("\n1.Append at end \t 2.Inserting element at specified position\t 3.Search\t 4.list of element starting with letter\t 5.Size\t 6.remove\t 7.Sort\t 8.Display\t");
      System.out.println("\nEnter your choice : ");
      c=Integer.parseInt(in.readLine());
      switch(c)
      {
          case 1:
          {
              System.out.println("\nEnter the string: ");
              str=in.readLine();
              obj.add(str);
              break;
          }
          case 2:
          {
              System.out.println("\nEnter the string: ");
              str=in.readLine();
              System.out.println("\nEnter the position to instert:");
              i=Integer.parseInt(in.readLine());
              obj.add(i-1,str);
              System.out.println("\nThe elements in the array list: ");
              break;
          }
          case 3:
          {
              System.out.println("\nEnter the element to search: ");
              str=in.readLine();
              j=obj.indexOf(str);
              if(j==-1)
              {
                  System.out.println("\nElement not found..");
              }
              else
              {
                  System.out.println("\nIndex of "+str+" is "+j);
              }
              break;
          }
          case 4:
          {
              System.out.println("\nEnter the character to list string starting with specified letter:");
              str=in.readLine();
              for(i=0;i<(obj.size()-1);i++)
              {
                  str1=obj.get(i);
                  if(str1.startsWith(str))
                  {
                      System.out.println(str1);
                  }
            }
            break;
          }
          case 5:
          {
              System.out.println("\nSize of the elemnets in array list is:"+obj.size());
              break;
          }
          case 6:
          {
              System.out.println("\nEnter the element to remove: ");
              str=in.readLine();
              if(obj.remove(str))
              {
                  System.out.println("\nElement Removed");
              }
              else 
              {
                  System.out.println("\nElement not found..");
              }
              break;

          }
          case 7:
          {
              Collections.sort(obj);
              System.out.println("Elements in the array list"+obj);
              break;
          }
          case 8:
          {
              System.out.println("Element in the array: "+obj);
              break;
          }

      }
      System.out.println("1 or 0");
      ch=Integer.parseInt(in.readLine());


      }while(ch==1);


  }  
}
