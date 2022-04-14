import java.util.*;

class ebill
{
public static void main(String args[])
{
customerdata ob=new customerdata();
ob.getdata();
ob.calc();
ob.display();
}
}
class customerdata
{
    Scanner in=new Scanner(System.in);
    Scanner ins= new Scanner(System.in);
    int bn;
    double previous,current,units,tbill;
    String cname,type;

void getdata()
{
 System.out.println("Enter consumer No.");
 bn=in.nextInt();
 System.out.println("Enter the type of connection:");
 type=ins.nextLine();
 System.out.println("Name:");
 cname=ins.nextLine();
 System.out.println("Enter per..");
 previous=in.nextDouble();
 System.out.println("current:");
 current=in.nextDouble();
}
void calc()
{
    units=current-previous;
    if(type.equals("D"))
    {
        if(units<=100)
        tbill= (1*units);
        else if(units>100 && units<=200)
        tbill= (2*units);
        else if(units>200 && units<=500)
        tbill= (4*units);
        else
        tbill= (6*units);
    }
    else
    {
        if(units<=100)
        tbill= (2*units);
        else if(units>100 && units<=200)
        tbill= (4.5*units);
        else if(units>200 && units<=500)
        tbill= (6*units);
        else
        tbill= (7*units);
    }
}
void display()
{
    System.out.println("Con no."+bn);
    System.out.println("Name"+cname);
    if(type.equals("D"))
    System.out.println("D");
    else
    System.out.println("C");
    System.out.println("Current"+current);
    System.out.println("Pre"+previous);
    System.out.println("units"+units);
    System.out.println("tbill"+tbill);
}
}