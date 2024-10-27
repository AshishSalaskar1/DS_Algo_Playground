package coinchange;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {
	
	static List<String> res = new ArrayList<>();
	
	static void CoinChange(int denoms[],int amount,String ans,int lastDenomIndex) {
		for (int i = lastDenomIndex; i < denoms.length; i++) {
			if (amount == 0)
			{
				res.add(ans);
				return;
			}
			if(amount<0)
				return;
			
			CoinChange(denoms, amount - denoms[i], ans+denoms[i], i);
		}
	}

	public static void main(String[] args) {
		int[] denoms = new int[] {2,3,5,6};
		int target = 10;
		
		CoinChange(denoms, target, "", 0);
		
		Iterator<String> it = res.listIterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
	}

}

