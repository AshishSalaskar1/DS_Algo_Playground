import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
     
     
	public static void main (String[] args) throws Exception
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //System.out.println();
	    
	    StringBuffer ans = new StringBuffer();
	    
	   // ans.append("strings");
	    
	    int T = Integer.parseInt(br.readLine());
	    
	    while(T-- > 0){
	        int n = Integer.parseInt(br.readLine());
	        String[] arr = br.readLine().trim().split(" ");
	        int[] a = new int[n];
	        for(int i=0;i<n;i++) a[i] = Integer.parseInt(arr[i]);
 	    }
 	    
 	     //System.out.println(ans);
 	 }
}
