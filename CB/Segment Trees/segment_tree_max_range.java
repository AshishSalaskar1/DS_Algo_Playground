package p1;

import java.util.*;
import java.io.*;

class Main {
    static  int[] a;
    static int[] st;
 
    static void buildMaxTree(int i,int start,int end) {
    	if(start == end)
    	{
    		st[i] = a[start];
    		return;
    	}
    	
    	int mid = (start+end)/2;
    	
    	buildMaxTree(2*i, start, mid);
    	buildMaxTree((2*i)+1, mid+1, end);
    	
    	st[i] = Math.max(st[2*i], st[2*i+1]);
    	

    }
    
    static int searchMaxTree(int i,int start,int end, int qS, int qE) {
    	
    	//totaly outside range
    	if(qS > end || qE < start)
    		return Integer.MIN_VALUE;
    	
    	//totally inside range 
    	if(start >= qS && end <= qE) 
    		return st[i];
    	
    	//overlaps
    	int mid = (start+end)/2;
    	int left = searchMaxTree(2*i, start, mid, qS, qE);
    	int right = searchMaxTree((2*i) +1 , mid+1, end, qS, qE);
    	
    	return Math.max(left,right);
    }

    static void updateTree(int i,int start,int end,int updateI) {
        //leaf : start == end == uI
        if(start == end) {
            st[i] = a[updateI];
            return;
        }
        
        int mid = (start+end)/2;
        
        if(updateI <= mid) updateTree(2*i, start, mid, updateI);
        else updateTree(2*i +1, mid+1, end, updateI);
        
        st[i] = Math.max(st[2*i] , st[2*i+1 ]);
    }

    public static void main(String args[] ) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int n = Integer.parseInt(br.readLine());
        a = new int[n+1];
        st = new int[4*(n+1)];
        String[] arr = br.readLine().trim().split(" ");
        
        //1-indexing is used
        for(int i=0;i<n;i++)
        	a[i+1] = Integer.parseInt(arr[i]);
        
        buildMaxTree(1, 1, n);
        
        System.out.println(searchMaxTree(1, 1, n, 1, 6));

         //change value at index 4 to 90
        a[4] = 90;
        updateTree(1, 1, n, 4);
        
        System.out.println(searchMaxTree(1, 1, n, 1, 6));
        

       
    }
}

/*
6
2 5 2 -3 4 -1
*/


