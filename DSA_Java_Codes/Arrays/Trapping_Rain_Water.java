import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
     
    static void doWork(int[] a,int n){
        int[] left = new int[n];
        int[] right = new int[n];
        
        left[0] = a[0];
        for(int i=1;i<n;i++)
            left[i] = Math.max(a[i],left[i-1]);
            
        right[n-1] = a[n-1];
        for(int i=n-2;i>=0;i--)
            right[i] = Math.max(a[i],right[i+1]);
        
        // for(int x : left)
        //     System.out.print(x+ " ");
        // System.out.println();
        
        // for(int x : right)
        //     System.out.print(x+ " ");
        // System.out.println();
            
        
        int ans = 0;
        
        for(int i=1;i<n-1;i++){
            int curWater = Math.min(left[i],right[i]) - a[i];
            
            ans += curWater > 0 ? curWater : 0;
        }
        
        System.out.println(ans);
        
    }
     
	public static void main (String[] args) throws Exception
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //System.out.println();
	    int T = Integer.parseInt(br.readLine());
	    
	    while(T-- > 0){
	        int n = Integer.parseInt(br.readLine());
	        String[] arr = br.readLine().trim().split(" ");
	        int[] a = new int[n];
	        for(int i=0;i<n;i++) a[i] = Integer.parseInt(arr[i]);
	        
	        doWork(a,n);
 	    }
 	 }
}
