/*Given N numbers, calculate sum of their factorial modulo 107. (Note it is not 10^7)

Input Format
First line contains positive integer N and the next line contains N space separated integers.

Constraints
N <= 10 and all integers lie between 0 and 1000.

Output Format
Output a single line denoting the result.

Sample Input
3
3 4 5

Sample Output
43

Explanation
3! = 6
4! = 24
5! = 120
(6 + 24 + 120) % 107 = 43
*/

import java.util.*;

public class Main {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
       
        int[] fact = new int[10002];
        fact[0] = 1;
        for(int i=1;i<=1001;i++)
            fact[i] = (fact[i-1]*i)%107;
        
        // for(int i=1;i<20;i++){
        //     System.out.println(fact[i]);
        // }
        
        int[] res = new int[N];
        int ans=0,temp;
        for(int i=0;i<N;i++){
            temp = in.nextInt();
            ans = ans+fact[temp];
        }
        System.out.print(ans%107);
   
    }
}