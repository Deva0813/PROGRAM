import java.util.*;

class NegativeAmtException extends Exception

{
    String msg;
    NegativeAmtException(String msg)    
    {
        this.msg=msg;
    }
    public String toString()
    {
        return msg;
    }
}








    class userdefine
    {
        public static void main(String[] args)
        {
           
            Scanner s=new Scanner(System.in);
            System.out.print("Enter the amount:");                                  //main
            int a=s.nextInt();
        try
            {       
                if(a<0)
                {
                throw new NegativeAmtException("Invaild amount");    //exception
                }    
                System.out.println("Amount deposited:"); 
            }
        catch(NegativeAmtException e)
        {
            System.out.println(e);
        }    
    }
}