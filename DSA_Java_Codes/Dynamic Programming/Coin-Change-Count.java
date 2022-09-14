package p1;

import java.util.*;




public class Main {
	
	 static int countCoinChange(int[] coins,int sum,int index) {
		 if(sum == 0) return 1;
		 
		 if(sum < 0) return 0;

		 
		 if(index <= 0 && sum!=0) return 0;
		 
		 return 
				 countCoinChange(coins, sum, index-1)+
				 countCoinChange(coins, sum - coins[index-1], index);
	 }
	 
	 static int test2(int[] coins,int sum,int index,int n) {
		 if(sum == 0) return 1;
		 
		 if(sum < 0) return 0;
		 
		 if(index == n && sum!=0) return 0;
		 
		 return
				 test2(coins, sum, index+1, n)+
				 test2(coins, sum - coins[index], index, n);
	 }
	
	

    public static void main(String args[]) {
    	Scanner in = new Scanner(System.in);
    
    	int[] coins = {1,2};
//    	System.out.println(countCoinChange(coins, 4, coins.length));
    	System.out.println(test2(coins, 4, 0, coins.length));

    }
}

