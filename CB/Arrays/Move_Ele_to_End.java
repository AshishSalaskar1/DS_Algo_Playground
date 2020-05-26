package p1;

import java.util.*;



public class Main {

	static void printArr(int[] arr) {
		for(int x : arr)
    		System.out.print(x+" ");
		System.out.println();
	}
	
	static void moveToLast(int[] a,int n,int key) {
		int i =0 ;
		int j = n-1;
		
		while(i < j) {
			while(a[j] == key)
				j--;
			
			while(a[i] != key)
				i++;
			
			if( i<j)
			{
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
		
	}
	
	static void moveLastStable(int[] a,int n,int key) {
		int cur = 0;
        int low = 0;
        
        while( cur < n){
            if(a[cur] != key ){
                //swap values
                int temp = a[cur];
                a[cur] = a[low];
                a[low] = temp;
                
                cur++;
                low++;
            }
            else
                cur++;
        }
	}
	
		
    public static void main(String args[]) {

    	int[] arr = {0,2,3,6,5,0,4,1,0,12,0,1,0};
    	int n = arr.length;
    	
    	moveToLast(arr,n);
//    	moveLastStable(arr,n,0);
    	
    	for(int x : arr)
    		System.out.print(x+" ");
    }
}


