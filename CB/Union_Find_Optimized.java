package p1;

import java.util.*;
import java.io.*;

class UnionFind{
	int[] parent;
	int[] size;
	
	UnionFind(int N){
		parent = new int[N+1];
		size = new int[N+1];
		
		for(int i=0;i<N;i++)	parent[i] = i;
	}
	
	int root(int i) {
		while( parent[i] != i) {
			
			//path compression
			// connect vis node to its grandparent
			parent[i] = parent[parent[i]];
			i = parent[i];
		}
		
		return i;
	}
	
	boolean isConnected(int a,int b) {
		return this.root(a) == this.root(b);
	}
	
	void union(int u,int v) {
		int a = this.root(u);
		int b = this.root(v);
		
		if(a == b) return;
		
		//attach shorter tree to larger one 
		if(size[a] < size[b]){
			 parent[a] = b;
			 size[b] += size[a];
		}
		else {
			parent[b] = a;
			size[a] += b;
		}
		
	}
}

class Main {
	
    public static void main(String args[] ){
    	
    	UnionFind u = new UnionFind(5);
    	
    	u.union(1, 2);
    	u.union(3, 5);
    	u.union(2, 4);
//    	u.union(1, 2?);
    	System.out.println(u.isConnected(1, 4));
    	System.out.println(u.isConnected(1, 5));
    	System.out.println(u.isConnected(3, 5));
    	
    	System.out.println(u.root(4));
    	
    }

}
