package JAVA.single;

class TNGovt {
    void pubg(){System.out.println("PUBG...\n");}  
    }  
    class Game extends TNGovt{  
    void ban(){System.out.println("\nBanned..  :(");}  
    }  
    class deva{  
    public static void main(final String args[]) {
        final Game d = new Game();
    d.ban();  
    d.pubg();  
    }}