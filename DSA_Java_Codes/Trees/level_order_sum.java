
import java.util.*;

import java.util.ArrayList;
import java.util.Scanner;

class  GenericTree{
	class Node{
		int data;
		ArrayList<Node> children = new ArrayList<>();
		Node(int data){
			this.data = data;
		}
	}
	
	Node root = null;
	int size = 0;
	Scanner in = new Scanner(System.in);
	
	GenericTree() {
		this.root = insertNode(null, 0);
	}
	
	Node insertNode(Node pNode,int ithchild) {
		Node node = new Node(in.nextInt());
		
		int childCount = in.nextInt();
		
		for(int i=0;i<childCount;i++) {
			Node childNode = insertNode(node, i);
			node.children.add(childNode);
		}
		
		size++;
		return node;
	
	}



	public void levelOrder(){
		 levelOrder(this.root);
	}
	
	class Pair{
		Node dNode;
		int lvl;
		
		Pair(Node dNode,int val){
			this.dNode = dNode;
			lvl = val;
		}
	}
	
	private void levelOrder(Node node) {
		int level = in.nextInt();
		LinkedList<Pair> q = new LinkedList<>();
		int res = 0;
		
		q.addLast(new Pair(node,0));
		while(!q.isEmpty()) {
			Pair rP = q.removeFirst();
			
			if(rP.lvl == level) {
				res+=  rP.dNode.data;
			}
			
			Node rn = rP.dNode;
			
//			System.out.print(rn.data+" ");
			for(Node n:rn.children) {
				q.addLast(new Pair(n,rP.lvl+1));
			}
			
		}
					
		System.out.println(res);
	}
}

public class Main {
    public static void main(String args[]) {
        GenericTree t = new GenericTree();

       t.levelOrder();

    }
}
