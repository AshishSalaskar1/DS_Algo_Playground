// { Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class DriverClass {
    public static void main(String[] args) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            ArrayList<ArrayList<Integer>> list = new ArrayList<>();
            String st[] = read.readLine().trim().split("\\s+");
            int edg = Integer.parseInt(st[0]);
            int nov = Integer.parseInt(st[1]);

            for (int i = 0; i < nov + 1; i++)
                list.add(i, new ArrayList<Integer>());

            String s[] = read.readLine().trim().split("\\s+");
            int p = 0;
            for (int i = 1; i <= edg; i++) {
                int u = Integer.parseInt(s[p++]);
                int v = Integer.parseInt(s[p++]);
                list.get(u).add(v);
            }

            int res[] = new int[10001];
            res = new TopologicalSort().topoSort(list, nov);
            boolean valid = true;

            for (int i = 0; i < nov; i++) {
                int n = list.get(res[i]).size();
                for (int j = 0; j < list.get(res[i]).size(); j++) {
                    for (int k = i + 1; k < nov; k++) {
                        if (res[k] == list.get(res[i]).get(j)) n--;
                    }
                }
                if (n != 0) {
                    valid = false;
                    break;
                }
            }
            if (valid == true)
                System.out.println("0");
            else
                System.out.println("1");
        }
    }
}
// } Driver Code Ends
/*Complete the function below*/

/*
ArrayList<ArrayList<>Integer>list: to represent graph containing 'N' vertices
                                    and edges between them
N: represent number of vertices
*/
class TopologicalSort {
    
    static int[] topoSort(ArrayList<ArrayList<Integer>> list, int V) {
        int[] inDegree = new int[V];
        int[] res = new int[V];
        int I = 0;
        
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
            res[I++] = src;
            
            for(int x : list.get(src)){
                inDegree[x]--;
                if(inDegree[x] == 0)
                    q.addLast(x);
            }
        }

        int[] Res = new int[V];
        I = 0;
        
        for(int i=res.length-1;i>=0;i--){
            Res[I++] = res[i];
        }
        return Res;
        
    }
}

