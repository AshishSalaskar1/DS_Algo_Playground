package java1;

import java.util.*;


public class Sol2 {
	
	static int startIndex;
	static int maxLength;
	
	
	
	
	
	static void subArraySumPositive(int[] a,int sum) {
		int n = a.length;
		
		int start=0;
		int end = 0;
		int curSum = a[0];
		
		while(end < n) {
			if(curSum == sum) {
				System.out.println(start+":"+end);
				return;
			}
			if(curSum < sum) {
				end++;
				if(end < n) curSum += a[end];
			}
			else {
				curSum = curSum - a[start++];
			}
		}
		
		System.out.println("No sum exists");
	}
	
	//KADANES Algo
	static void maxSubSum(int[] a) {
		int n = a.length;
		
		int start =0;
		int end = 0;
		
		int curMax = 0;
		int globalMax = Integer.MIN_VALUE;
		
		int ptr = 0;
		
		for(int i=0;i<n;i++) {
			curMax += a[i];
			
			//present sum is -ve so start from next index
//			if(curMax < 0) {
//				curMax = 0;
//				ptr = i+1;
//			}
			
			//present sum > globalMax
			if(curMax > globalMax) {
				globalMax = curMax;
				start = ptr;
				end = i;
			}
		}
		
		System.out.println("Max subarray sum: "+globalMax);
//		System.out.println("Indices: "+start+":"+end);
	}
	
	static void subArraySum(int[] a,int sum) {
		
		int n = a.length;
		int cSum=0;
		
		HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
		
		
		for(int i=0;i<n;i++) {
			cSum += a[i];
			
			
			
			if(sum == cSum) {
				System.out.println("0:"+i);
				return;
			}
			
			if(map.containsKey(cSum - sum))
			{
				System.out.println(map.get(cSum-sum)+":"+i);
				return;
			}
			
			map.put(cSum, i);
		}
		
		System.out.println("No sum exists");
	}
	
	
	public static void main(String[] args){
		
		int[] arr = {1,2,3,4,5,6,7,8};
		int[] b = {-1,14,-6,5};
		
		
//		subArraySumPositive(arr,7);
//		maxSubSum(arr);
//		subArraySum(arr, 5);
		maxSubSum(b);
		
		
    	
	}

}

