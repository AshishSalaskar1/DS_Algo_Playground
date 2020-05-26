package java1;

//Bit manipulation

import java.util.*;
class Sol2{
	
	static int no_of_set_bits(int n) {
		int count = 0;
		
		while(n!=0)
		{
			count += (n & 1);
			n = n>>1;
		}
		
		return count;
	}
	
	static int no_of_set_bits_faster(int n) {
		int count = 0;
		
		while(n!=0)
		{
			n = n & (n-1);
			count++;
		}
		
		return count;
	}
	
	static int setBit(int n,int k) {
		int mask = 1<<k;
		
		return n | mask;
	}
	
	static int unsetBit(int n,int k) {
		int mask = ~(1<<k);
		
		return n & mask;
	}
	
	public static void main(String[] args){

		System.out.println(no_of_set_bits(13));
		System.out.println(no_of_set_bits(13));
		
		System.out.println(setBit(13, 1));
		System.out.println(unsetBit(13, 2));
	}
		
}

