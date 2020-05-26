package java1;

//Aggresive Cows

import java.util.*;
class Sol2{
	
	static boolean canPlaceCows(int dist,int[] a,int c) {
		int cows = 1;
		int pos = a[0];
		
		for(int i=1;i<a.length;i++) {
			if(a[i] - pos >= dist) {
				pos = a[i];
				cows++;
				
				if(cows == c) return true;
			}
		}
		
		return false;
	}
	
	static int aggresiveCows(int[] a,int c) {
		Arrays.sort(a);
		int start = 0;
		int end = a[a.length-1];
		
		int res = -1;
		
		while(start < end) {
			int mid = (start+end)/2;
			
			if(canPlaceCows(mid, a, c)) {
				if(mid > res)
					res = mid;
				start = mid+1;
			}
			else {
				end = mid;
			}
		}
		
		return res;
		
		
	}
	
	public static void main(String[] args){
		int[] stalls = {1,2,8,4,9};
		int c = 3;
//		System.out.println(canPlaceCows(5,stalls,c));
		System.out.println(aggresiveCows(stalls, c));
	
	}
		
}

