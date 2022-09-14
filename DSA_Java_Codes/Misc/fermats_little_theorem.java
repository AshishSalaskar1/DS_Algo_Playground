package p1;

import java.util.*;
import java.io.*;

class Main {
	
	static int pow(int a,int n, int m){
        int res = 1;
        while(n > 0){
            if(n%2 != 0){
                res = (res * a) % m;
                n--;
            } 
            
            else{
                a = (a*a) % m;
                n /= 2;
            }
        }
        
        return res;
    }
	
	static long pow(long a,long n){
        long res = 1;
        while(n > 0){
            if(n%2 != 0){
                res = (res * a);
                n--;
            } 
            
            else{
                a = (a*a);
                n = n/2;
            }
        }
        
        return res;
    }
	
    public static void main(String args[] ){
//    	System.out.println(pow(45,86,88));
    	System.out.println(pow(45,86) % 88 );
    }

}
