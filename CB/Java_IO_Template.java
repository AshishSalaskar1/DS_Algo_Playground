import java.io.*;
import java.util.*;


public class Main {
	

    public static void main(String args[]) throws Exception{
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine().trim());
    	
    	int[] arr = new int[n];
    	
    	String[] sArr = br.readLine().trim().split(" ");
    	for(int i=0;i<n;i++) {
    		arr[i] = Integer.parseInt(sArr[i]);
    	}
    }
    
}


