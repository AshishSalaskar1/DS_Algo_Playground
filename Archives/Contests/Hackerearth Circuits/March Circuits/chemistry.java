//  package basic;

import java.io.*;
import java.text.*;
import java.util.*;

public class TestClass {

	
	static boolean areWholeNumbers(double a,double b) {

		 double A = ((long)(a*100000) ) / 100000.0;
		 double B = ((long)( b*100000) ) / 100000.0;

		 //Round x.000000001 to x
		 //Round x.99999 to x+1
		 
		return ( ((A == (long)a) || (float)(A%1)==0.99999f) 
				&& 
				((B == (long)b) || (float)(B%1)==0.99999f)
				);
		
	}
		

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a,b,c,d;
		String[] arr = br.readLine().trim().split(" ");
		
		a = Integer.parseInt(arr[0]);
		b = Integer.parseInt(arr[1]);
		c = Integer.parseInt(arr[2]);
		d = Integer.parseInt(arr[3]);
		
		double x = (double)c/a;
		double y = (double)d/b;
		
		double A = x;
		double B = y;
		int res = 1;
		
		while( !areWholeNumbers(A, B) ) {
			A = x*res;
			B = y*res;	
			res++;			
		}
		
		res--;

        System.out.println((int)(res*(double)c/a) + " "+(int)B+" "+(int)res);

		
	}	

}

