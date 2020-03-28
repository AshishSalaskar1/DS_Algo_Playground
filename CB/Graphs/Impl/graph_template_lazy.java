
import java.util.*;
import java.io.*;


class TestClass {

    static int V;
    static ArrayList<Integer>[] adj;
    static boolean[] vis = new boolean[100000];

    static void DFS(int src){
        vis[src] = true;
        for(int x : adj[src])
            if(!vis[x])
                DFS(x);
    }

    public static void main(String args[] ) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] init = br.readLine().trim().split(" ");
        V = Integer.parseInt(init[0]);

        adj = new ArrayList[V+1];

        for(int i=1;i<=V;i++)
            adj[i] = new ArrayList<>();

        
        int E = Integer.parseInt(init[1]);

        for(int i=0;i<E;i++){
            String[] in = br.readLine().trim().split(" ");
            int u = Integer.parseInt(in[0]);
            int v = Integer.parseInt(in[1]);

            adj[u].add(v);
            adj[v].add(u);
        }
        
        int count = 0;

        for(int i=1;i<=V;i++)
            if(!vis[i]){
                count++;
                DFS(i);
            }
        
        System.out.print(count);



    }
}

