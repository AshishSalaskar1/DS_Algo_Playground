package p1;

import java.util.*;

import java.io.*;


class Q{
	int L,R,I;
	public Q(int L,int R,int I) {
		this.L = L;
		this.R = R;
		this.I = I;
	}
	
	public String toString() {
		return L+":"+R;
	}
}

class Main
{	
	
	static int[] f = new int[1000000];
	static int count = 0;
	static int[] a;
	static int mL = 0,mR = 0;
	
	static void add(int pos) {
		f[a[pos]]++;
		if(f[a[pos]] == 1)
			count++;
	}
	
	
	static void remove(int pos) {
		f[a[pos]]--;
		if(f[a[pos]] == 0)
			count--;
	}
	
	static void doWork(ArrayList<Q> q) {
		int l,r;
		for(int i=0;i<q.size();i++) {
			l = q.get(i).L;
			r = q.get(i).R;
			
			while(l < mL)
				add(mL--);
			while(l > mL)
				remove(mL++);
			while(r > mR)
				add(mR++);
			while(r < mR)
				remove(mR--);
				
			System.out.println(l+":"+r+" = "+count);
		}
		
	}
	
	
	
	public static void main (String[] args) throws Exception
	{
		a = new int[]{1,2,2,3,4,1,2,4,5,3};
		ArrayList<Q> qs = new ArrayList<>();
		qs.add(new Q(1,3,1));
		qs.add(new Q(0,15,2));
		qs.add(new Q(1,6,3));
		
		System.out.println(qs);
		
		Collections.sort(qs, new Comparator<Q>() {
			@Override
			public int compare(Q q1, Q q2) {
				if(q1.L != q2.L)
					return Integer.valueOf(q1.L).compareTo(q2.L);
				else
					return Integer.valueOf(q1.R).compareTo(q2.R);
			}
		});
		
		
		System.out.println(qs);
		
		
	
		
	}
		
}
