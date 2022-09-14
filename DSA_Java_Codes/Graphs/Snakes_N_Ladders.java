package snakes;

import java.util.*;

//dice : 1-6 so each node n is connected to 6 nodes(n+1 -> n+6)

class Node{
	int noOfRolls;
	int v;
}


public class Snakes_Ladders {
	
	
	//BFS
	static int findMinRolls(int[] board, int N) {
		boolean[] vis = new boolean[N+1];
		LinkedList<Node> q = new LinkedList<>();
		vis[1]=true;
		
		Node node = new Node();
		node.noOfRolls = 0;
		node.v = 0;
		
		q.addLast(node);
		
		while(!q.isEmpty()) {
			node = q.removeFirst();
			int rV = node.v;
			
			//last box reached
			if(rV == (N-1)) break;
			
			//visit al neighbours - dice ans 1-6
			for(int i=rV+1; i<= rV+6 && i<=N ;i++) {
				if(!vis[i]) {
					Node iNode = new Node();
					iNode.noOfRolls = 1 + node.noOfRolls;
					
					vis[i] = true;
					
					//check if it is snake or ladder
					if(board[i] != 0)
						iNode.v = board[i];
					else
						iNode.v = i;
					
					//add to queue
					q.add(iNode);
				}
			}
			
			
		}
		
		return node.noOfRolls;
		
	}


	public static void main(String[] args) {
		// 30 x 30 board
		int N = 30;
		
		int[] board = new int[N+1];
		
		// Ladders 
		board[2] = 21; 
		board[4] = 7; 
		board[10] = 25; 
		board[19] = 28; 

		// Snakes 
		board[26] = 0; 
		board[20] = 8; 
		board[16] = 3; 
		board[18] = 6; 
		
		int res = findMinRolls(board, N);
		
		System.out.println("Minimum No of dice rolls needed: "+res);
		
		
		

	}

}

