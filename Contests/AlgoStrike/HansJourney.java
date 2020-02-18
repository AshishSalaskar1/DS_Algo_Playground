package p1;

import java.util.*;


class Job{
	int start,end,profit;

	public Job(int start, int timeToComplete, int profit) {
		this.start = start;
		this.end = start+timeToComplete;
		this.profit = profit;
	}
	
//	public Job1(int start, int end, int profit) {
//		this.start = start;
//		this.end = end;
//		this.profit = profit;
//	}
	
	
}

public class Main {

    public static void main(String args[]) {
    	Scanner in = new Scanner(System.in);
    	int n = in.nextInt();
    	Job[] a = new Job[n];
    	
    	for(int i=0;i<n;i++) {
    		a[i] = new Job(in.nextInt(),in.nextInt(),in.nextInt());
    	}
    	

    	Arrays.sort(a,new Comparator<Job>() {
    		public int compare(Job a,Job b) {
    			return Integer.valueOf(a.end).compareTo(b.end);
    		}
    	});
    	
//    	for(Job x : a) System.out.print(x.profit+" ");
//    	System.out.println();
    	
    	Integer[] res = new Integer[n];
    	
    	for(int i=0;i<n;i++) res[i] = a[i].profit;
    	
    	
    	
    	int maxProfit;
    	
    	for(int i=1;i<n;i++) {
    		
    		for(int j=i-1;j>=0;j--) {
    			if(a[i].start >= a[j].end) {
    				maxProfit = res[j] + a[i].profit;
    				res[i] = Math.max(res[i], maxProfit);
    			}
    		}
    		
    	}
    	
//    	for(Integer x: res) System.out.print(x+" ");
//    	System.out.println();
    	
    	System.out.println(Collections.max(Arrays.asList(res)));

    	
    }
}

/*
4
1 2 50
2 2 10
3 2 40
3 3 70

op: 120
*/