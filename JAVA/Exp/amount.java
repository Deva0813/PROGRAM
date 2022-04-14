import java.util.*;

class amount
{
    public static void main(String args[])
    {
    Scanner n=new Scanner(System.in);
    int a;
    System.out.println("Enter amount:");
    a=n.nextInt();

    if(a>0)
    {
        System.out.println("Amount deposited...");
    }
    else
    {
        System.out.println("Invalid amount...");
    }
    }

}