// package java1;

import java.io.*;
import java.util.*;


import java.math.*;


class Pair{
	int a,b;
	Pair(int a,int b){
		this.a = a;
		this.b = b;
	}
	
	public String toString() {
		return a+","+b;
	}
}

class Graph{
	
	ArrayList<Pair> ans = new ArrayList<>();
	
	int V;
	ArrayList<Integer>[] adj;
	
	Graph(int V){
		this.V = V;
		adj = new ArrayList[V+1];
		for(int i=1;i<=V;i++) {
			adj[i] = new ArrayList<Integer>();
		}
	}
	
	void addEdge(int u,int v) {
		this.adj[u].add(v);
		this.adj[v].add(u);
	}
	
	void removeEdge(int u,int v) {
		this.adj[u].remove(Integer.valueOf(v));
		this.adj[v].remove(Integer.valueOf(u));
	}
	

	
	//count no of nodes in each component
	int dfs(int src) {
		boolean[] vis = new boolean[V+1];
		vis[src] = true;
		int count = 0;

	
		dfsUtil(src, -1, vis);
		
		for(boolean x : vis)
			if(x) count++;

		return count;
	}
	
	private void dfsUtil(int src,int parent,boolean[] vis) {
		vis[src] =true;
		
		for(int x : adj[src])
			if(!vis[x])
				dfsUtil(x, src,vis);	
	}

	
	ArrayList<Pair> bridge(int src) {
		int timer = 0;
		int[] in = new int[V+1];
		int[] low = new int[V+1];

        Arrays.fill(in,-1);
        Arrays.fill(low,-1);
		boolean[] vis = new boolean[V+1];
		
		bridgeUtil(src, -1, vis, low, in, timer);
		
		return this.ans;
		
		
	}
	
	private void bridgeUtil(int src,int parent,boolean[] vis,int[] low,int[] in,int timer) {
		timer++;
		in[src] = low[src] = timer;
		
		vis[src] = true;
		

			for(int child : adj[src]) {
				
				if(child == parent) continue;
				
				if(vis[child]) 
					low[src] = Math.min(low[src], in[child]);

				else {
					bridgeUtil(child, src, vis, low, in, timer);

					if(low[child] > in[src])
						this.ans.add(new Pair(src,child));

					low[src] = Math.min(low[src], low[child]);
				}
			}

		
	}


	boolean breakBridge(int u,int v) {
//		System.out.println("Bridge: "+u+"<->"+v);
		this.removeEdge(u, v);
		
		int count1 = this.dfs(u);
		int count2 = this.dfs(v);
		
//		System.out.println(count1+" ::: "+count2);
		
		this.addEdge(u, v);
		
		if((count1%2 != 0) || (count2%2 != 0))
			return false;
			
		return true;
	}



}

public class TestClass {
	
	public static void main(String[] args) throws Exception{


		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] init = br.readLine().trim().split(" ");
		int V = Integer.parseInt(init[0]);
		int E = Integer.parseInt(init[1]);
				
		Graph a = new Graph(V);
		
		while(E-- > 0) {
			String[] arr = br.readLine().trim().split(" ");
			a.addEdge(Integer.parseInt(arr[0]),Integer.parseInt(arr[1]));
		}
		
		
		int A,B;
		A = B = 0;

        int nBridges = 0;


        a.DFS(1);
        ArrayList<Pair> res= a.bridge(1);
        nBridges = res.size();
        for(Pair x: res)
            if(a.breakBridge(x.a, x.b))
                A++;
            else
                B++;


		
	
		
//		System.out.println(nBridges);

		if(A == 0) {
			System.out.println("0 1");
		}
		else {
			BigInteger MOD = BigInteger.valueOf((long) (Math.pow(10, 9)+7));
			
			BigInteger res1 = BigInteger.valueOf(nBridges).modInverse(MOD).multiply(BigInteger.valueOf(A));
			BigInteger res2 = BigInteger.valueOf(nBridges).modInverse(MOD).multiply(BigInteger.valueOf(B));

			System.out.println(res1+" "+res2);
		}

		
//		System.out.println(A+" <=> "+B);
	
	}

}
/*


100000 7
1 2
2 3
3 1
4 5
5 6
6 4
1 4

*/
