package java1;

import java.io.*;
import java.util.*;

public class Sol2 {
  
  static void doWork(String fileName) throws IOException {
    File file = new File("/home/ashish/Desktop/Hashcode/"+fileName+".in"); 
      Scanner in = new Scanner(file);

        int Max = in.nextInt();
        
        int n = in.nextInt();
        int[] a = new int[n];
        for(int i=0;i<n;i++) a[i] = in.nextInt();
        
        String MainAns = "";
        int maxSlices = 0;
        
//        System.out.println(n-1);
        
       for(int I=n-1;I>=0;I--) {
         HashMap<Integer,Integer> hs = new HashMap<>();
          
         int max = Max;
         int slices = 0;
         
           for(int i=I;i>=0;i--) {
            if(a[i] <= max) {
              hs.put(i, -1);
              max -= a[i];
              slices += a[i];
            }
            
            if(max == 0) break;
           }
           
//           System.out.println("Slices: "+slices);
           
           if(slices < maxSlices) continue;
           
           else maxSlices = slices;
           
           
           String ans = "";
           
           
           ans = ans + hs.size()+"\n";
           for(int x: hs.keySet())
              ans = ans + x+ " ";
           
           MainAns = ans;
       }
        
        in.close();
 
        FileWriter myWriter = new FileWriter("/home/ashish/Desktop/Hashcode/out/"+fileName+".out");
        myWriter.write(MainAns);
//        System.out.println(MainAns);
        myWriter.close();
        
  }


    public static void main(String args[]) throws IOException {
      
//      doWork("ash");
      doWork("a_example");
      doWork("b_small");
      doWork("c_medium");
      doWork("d_quite_big");
      doWork("e_also_big");
      System.out.println("DONe");
      
      
    }
}