import java.io.*;

interface stackoperation
{
    public void push(int i);
    public void pop();
}
 class Astack implements stackoperation
 {
     int stack[]=new int[5];
     int top=-1;
     int i;
     public void push(int item)
     {
         if(top>=4)
         {
             System.out.println("overflow");
         }
         else
         {
             top=top+1;
             stack[top]=item;
             System.out.println("item pushed: "+stack[top]);
         }
     }
     public void pop()
     {
         if(top<0)
         {
             System.out.println("underflow");
         }
         else
         {
             top=top-1;
            System.out.println("\nmElement poped: "+stack[top]);
         }
    
     }
     public void display()
     {
         if(top<0)
         {
             System.out.println("No Element in stack");
         }
         else
         {
             for(i=0;i<=top;i++)
             System.out.println("Element :"+stack[i]);
         }
     }

 }
 class teststack
 {
     public static void main(String args[])throws IOException
     {
         Astack s=new Astack();
         DataInputStream in=new DataInputStream(System.in);
         int c,ch;
         int i;
         do
         {
         try
         {
         System.out.println("Array Stack");
         System.out.println("\n1.push\t 2.pop\t 3.diaplay\t 4.exit");
         System.out.println("\nEnter your choice: ");
         c=Integer.parseInt(in.readLine());
         switch(c)
         {
             case 1:
             {
                 System.out.println("Enter the element:");
                 i=Integer.parseInt(in.readLine());
                 s.push(i);
                 break;
             }
             case 2:
             {
                 s.pop();
                 break;
             }
             case 3:
             {
                 s.display();
                 break;
             }
             case 4:
             {
                 break;
             }

         }
        }
         catch(IOException e)
         {
             System.out.println("Io error");
         }
        System.out.println("1 or 0");
         ch=Integer.parseInt(in.readLine());
         

        }while(ch==1);

     }
 }
