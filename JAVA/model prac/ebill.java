import java.util.*;

class ebill
{
    public static void main(String args[])
    {
     customerdata ob =new customerdata();
     ob.getdata();
     ob.calc();
     ob.display();
    }
}
class customerdata
{
    Scanner in=new Scanner(System.in);
    Scanner ins=new Scanner(System.in);
    int bn;
    String name,type;
    double pre,cur,units,tbill;
    
    void getdata()
    {
        System.out.println("Enter customer .no.");
        bn=in.nextInt();
        System.out.println("name ");
        name=ins.nextLine();
        System.out.println("Enter the type.. ");
        type=ins.nextLine();
        System.out.println("Prev..: ");
        pre=in.nextDouble();
        System.out.println("Current...: ");
        cur=in.nextDouble();
    }
    void calc()
    {
        units=cur+pre;
        if(type.equals("D"))
        {
            if(units<=100)
            tbill=units*1;
            else if(units>100 && units<=200)
            tbill=units*2.50;
            else if(units>200 && units<=500)
            tbill=units*4;
            else 
            tbill=units*6;
        }
        else
        {
            if(units<=100)
            tbill=units*2;
            else if(units>100 && units<=200)
            tbill=units*4.50;
            else if(units>200 && units<=500)
            tbill=units*6;
            else 
            tbill=units*7;
        }

    }
    void display()
    {
        System.out.println("Customer no.: "+bn);
        System.out.println("Name: "+name);
        if(type.equals("D"))
        System.out.println("Type of is Domestic...");
        else
        System.out.println("Type of connection is commercial");
        System.out.println("previous...: "+pre);
        System.out.println("current...:"+cur);
        System.out.println("total units..: "+units);
        System.out.println("Total bill: "+tbill);
    }
}