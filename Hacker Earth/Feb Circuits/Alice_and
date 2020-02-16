import java.util.*;

public class Main {

    static HashSet<Integer> set = new HashSet<>();

    static void iss(int[] a,int index,int sum,int n){

        if(sum % 2 == 0 && sum != 0) {
            if(!set.contains(sum))
                set.add(sum);
        }

        if(index == n) return;

        iss(a,index+1,sum+a[index],n);
        iss(a,index+1,sum,n);
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        
        for(int i=0;i<n;i++) arr[i] = in.nextInt();

        iss(arr,0,0,arr.length);
        System.out.println(set.size());
    }
}
