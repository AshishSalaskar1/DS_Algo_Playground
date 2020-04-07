package p1;

import java.util.*;
import java.lang.*;
import java.io.*;


class Interval{
	int buy,sell;

	public String toString() {
		return this.buy+":"+this.sell;
	}
}

class Main
 {
	static void stockSpan(int[] prices,int n) {
		
		if(n==1) return;
	
		ArrayList<Interval> res = new ArrayList<>();
		
		int i=0;
		int count=0;
		
		while(i < n-1) {
			//finding local minima (a<b) ie stock prices fall next day
			while( (i < n-1) && prices[i]>=prices[i+1])
				i++;
			
			if(i == n-1) break;
			
			Interval I = new Interval();
			I.buy = i;
			
			//start searching for maxima from next
			i++;
			
			while( (i < n) && prices[i] >= prices[i-1])
				i++;
			
			//bcause i++ is done
			I.sell = i-1;
			res.add(I);
			
			count++;
			
		}
		
		System.out.println(res);
		
		int maxProfit = 0;
        
       	        for(Interval x : res)
           		maxProfit += (prices[x.sell] - prices[x.buy]);	
 		}
	

	

	public static void main (String[] args) throws Exception
	 {
		int[] arr = {100,180,260,310,40,535,695};
		
//		stockSpan(arr, arr.length);
		stockSpan(arr, arr.length);
	  
 	 }
}
