// { Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class DriverClass
{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            ArrayList<ArrayList<Integer>> list = new ArrayList<>();
            int nov = sc.nextInt();
            int edg = sc.nextInt();
            for(int i = 0; i < nov+1; i++)
                list.add(i, new ArrayList<Integer>());
            for(int i = 1; i <= edg; i++)
            {
                int u = sc.nextInt();
                int v = sc.nextInt();
                list.get(u).add(v);
            }
            if(new DetectCycle().isCyclic(list, nov) == true)
                System.out.println("1");
            else System.out.println("0");
        }
    }
}// } Driver Code Ends
/*Complete the function below*/

/*
ArrayList<ArrayList<Integer>> list: to represent graph containing 'v'
                                    vertices and edges between them
V: represent number of vertices
*/
class DetectCycle
{
   static boolean[] vis;
    
  
    
    static boolean isCyclic(ArrayList<ArrayList<Integer>> list, int V)
    {
        int[] inDegree = new int[V];
        int count = 0;
        
        for(ArrayList<Integer> x : list){
            for(int y: x)
                inDegree[y]++;
        }
        
        LinkedList<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++){
            if(inDegree[i] == 0)
                    q.addLast(i);
        }
                
        while(!q.isEmpty()){
            int src = q.removeFirst();
            count++;
            
            for(int x : list.get(src)){
                inDegree[x]--;
                if(inDegree[x] == 0)
                    q.addLast(x);
            }
        }
        
        if(count == V) return false;
        else return true;
        
        
    }
}
