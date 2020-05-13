package p1;

import java.util.*;
import java.io.*;

class UF{
	int[] par;
	UF(int N){
		par = new int[N+1];
		for(int i=0;i<=N;i++)	par[i] = i;
	}
	
	int root(int i) {
		while(par[i] != i) {
			par[i] = par[par[i]];
			i = par[i];
		}
		
		return i;
	}
	
	boolean union(int u,int v) {
		int a = this.root(u);
		int b = this.root(v);
		
		if(a==b) return false;
		
		par[a] = b;
		
		return true;
	}
}

class Main {
	
	static class Edge{
		int u,v,wt;

		public Edge(int u, int v, int wt) {
			this.u = u;
			this.v = v;
			this.wt = wt;
		}
		
		public String toString() {
			return u+":"+v+"=>"+wt;
		}
		
	}
	
    public static void main(String args[] ){
    	
    	Scanner in = new Scanner(System.in);
    	
    	int n = in.nextInt();
    	int e = in.nextInt();
    	
    	UF uf = new UF(n+1);
    	
    	ArrayList<Edge> arr = new ArrayList<>();
    	
    	while(e-- > 0) {
  
    		int a = in.nextInt();
    		int b = in.nextInt();
    		int wt = in.nextInt();
    		arr.add(new Edge(a,b,wt));
    	}
    	
    	Collections.sort(arr,new Comparator<Edge>() {
    		public int compare(Edge u,Edge v) {
    			return Integer.valueOf(u.wt).compareTo(v.wt);
    		}
    	});
    	
    	System.out.println();
    	System.out.println(arr);
    	
    	int addCount  = 0;
    	int cost = 0;
    	for(Edge x : arr) {
    		if(uf.union(x.u, x.v))
    		{
    			addCount++;
    			cost += x.wt;
    			System.out.println("Added: " +x);
    		}
    		
    		if(addCount == (n-1)) break;
    		//check is MST formed already
    	}
    	
    	System.out.println(cost);
    	
    }
}

/*
 * INPUT FORMAT
 * N(nodes) E(Edges)
 * u v weight... E times
 * Print cost of MST else -1 if no MST
 * */

