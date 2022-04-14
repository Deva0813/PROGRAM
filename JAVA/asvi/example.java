class MyException extends Exception
{
    String str1;
    MyException(String str2)
    {
        str1=str2;
    }
    public String toString()                                                 
    {
    return ("MyException Occurred: "+str1) ;
    }
    }


    class example
    {
    public static void main(String args[])
    {
    try
    {
    throw new MyException("This is My error Message\n");
    }
    catch(MyException exp)
    {
    System.out.println(exp) ;
    }
    }
}