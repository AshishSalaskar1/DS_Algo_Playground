package basic;

import java.io.*;
import java.util.*;

public class Main {
		

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long N = Long.parseLong(br.readLine());
		System.out.println(N);
		int key,val;
		
		HashMap<Integer, Set<Integer> > map = new HashMap<>();
		
		int[][] a = new int[10][10];
		
		for(int i=0;i<10;i++) {
			String[] arr = br.readLine().trim().split(" ");
			for(int j=0;j<10;j++)
					a[i][j] = Integer.parseInt(arr[j]);
		}
		
		for(int i=0;i<10;i++) {
			 key = a[i][0];
			
			for(int j=1;j<10;j++) {
				val = a[i][j];
				
				if(!map.containsKey(key)) {
					map.put(key,new HashSet<Integer>());
				}
				map.get(key).add(val);
				
				if(!map.containsKey(val)) {
					map.put(val,new HashSet<Integer>());
				}
				map.get(val).add(key);
			}
		}
		
		

		int count = 0;
		for(Set<Integer> x : map.values()) {
//			System.out.println(x+" count: "+x.size());
			count += x.size();
		}
		
//		System.out.println(count);
//
		System.out.println( (long)(N*(N-1)/2)  - (int)(count/2));

//		System.out.println((N*(N-1)));
		
		
	}	

}

