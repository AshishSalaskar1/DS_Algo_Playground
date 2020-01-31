package p1;

import java.util.*;

//Sub Array sum
class Solution {
	
	//only works for positive numbers
	static void subSum1(int[] a,int sum) {
		int start = 0,end =0;
		int curSum = a[0];
		int n = a.length;
		
		while(end < n) {
			if(curSum == sum) {
				System.out.println("Subarray indices: "+start+" -> "+end);
				return;
			}
			if(curSum <= sum) {
				end++;
				if(end<n)	curSum += a[end];
			}
			else {
				curSum = curSum - a[start++];
			}
		}
		
		System.out.println("NOT FOUND");
	}
	
	//works for negative and positive
	static void subSum2(int[] a,int sum) {
		int n = a.length;
		
		HashMap<Integer,Integer> map = new HashMap<>();
		
		int curSum = 0;
		
		for (int i = 0; i < a.length; i++) {
			curSum += a[i];
			
			if(curSum == sum) {
				System.out.println("Subarray indices: 0 -> "+i);
				return;
			}
			
			if(map.containsKey(curSum-sum)) {
				System.out.println("Subarray indices: "+(map.get(curSum-sum)+1)+" -> "+i);
				return;
			}
			
			map.put(curSum, i);
		}
		
		System.out.println("NOT FOUND");
	}
	
	public static void main(String[] args) {
		
		int[] a = {1,4,5,2,45,6,2,};
		int[] b = {1,4,5,10,45,-5,2,};
		
//		subSum1(a, 1156);
		subSum2(b,50);
	
	}
	


}



