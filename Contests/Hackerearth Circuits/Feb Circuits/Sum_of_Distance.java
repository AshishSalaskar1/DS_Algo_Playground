import java.util.*;
 
class TestClass {
    public static void main(String args[] ) throws Exception {
       
       Scanner in = new Scanner(System.in);
       
       int n;
       n = in.nextInt();
       
       double temp;
       double sum=0;
       
       for(int i=0;i<n;i++){
           temp = in.nextInt();
           
           sum = sum + ((Math.sin(2*temp))/2);
       }
       
       double res = (n-1) * sum;
       System.out.printf("%.2f",res);
 
    }
}
