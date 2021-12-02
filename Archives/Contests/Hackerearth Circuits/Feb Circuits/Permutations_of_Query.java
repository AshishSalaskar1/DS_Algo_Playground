import java.util.*; 
import java.lang.Math;

class Main 
{ 

    static int[] minDistance(int n, int k, int point[][]) 
    { 
        

        for (int i = 0; i < k; i++) 
            Arrays.sort(point[i]); 

        int[] res = new int[4];

        for (int i = 0; i < k; i++) {
            // System.out.print(point[i][(int) Math.ceil((double)(n / 2) - 1)] + " "); 
            res[i] = point[i][(int) Math.ceil((double)(n / 2) - 1)];
        }
        return res;
    } 

    static int distance(int[][] a,int src,int dest){
        return Math.abs(a[0][src] - a[0][dest])+Math.abs(a[1][src] - a[1][dest])+
        Math.abs(a[2][src] - a[2][dest])+Math.abs(a[3][src] - a[3][dest]);
    }

    static int distance(int[][] a,int src,int[] dest){
        // System.out.println(a[0][src]+" : "+a[1][src]+" : "+a[2][src]+" : "+a[3][src]);

        return 
        Math.abs(a[0][src] - dest[0])+
        Math.abs(a[1][src] - dest[1])+
        Math.abs(a[2][src] - dest[2])+
        Math.abs(a[3][src] - dest[3]);
    }


    public static void main(String[] args) 
    { 
        // int n = 3; 
        int k = 4; 
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int[][] point = new int[4][n];
        for(int i=0;i<n;i++){
            point[0][i] = in.nextInt();
            point[1][i] = in.nextInt();
            point[2][i] = in.nextInt();
            point[3][i] = in.nextInt();
        }

        int[][] a = new int[4][n];

        for(int i=0;i<n;i++){
            a[0][i] = point[0][i];
            a[1][i] = point[1][i];
            a[2][i] = point[2][i];
            a[3][i] = point[3][i];
        }
        
     
        // Hash
        int[] minPoint = minDistance(n, k, point); 

        // for(int x : minPoint) System.out.print(x);
        // System.out.println();



        HashMap<Integer,Integer> map =new HashMap<>();

        for(int i=0;i<n;i++){
            int dist = distance(point,i,minPoint);
            map.put(i,dist);
        }
        
        for(int key : map.keySet())
            System.out.print((key+1)+" ");

        
    } 
} 


