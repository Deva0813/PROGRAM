interface Showable{  
  void show();  
  interface Message{  
   void msg();  
  }  
}  
class interface1 implements Showable.Message{  
 public void msg(){System.out.println("\nHello nested interface\n");}  
  
 public static void main(String args[]){  
  Showable.Message message=new interface1();//upcasting here  
  message.msg();  
 }
} 
