// Link : https://leetcode.com/problems/move-zeroes


//stable and better
class Solution {
    
    static void moveLastStable(int[] a,int n,int key) {
		int cur = 0;
        int low = 0;
        
        while( cur < n){
            if(a[cur] != key ){
                //swap values
                int temp = a[cur];
                a[cur] = a[low];
                a[low] = temp;
                
                cur++;
                low++;
            }
            else
                cur++;
        }
	}
    
    public void moveZeroes(int[] a) {
   
        moveLastStable(a,a.length,0);
    }
}

// Stable 
class Solution {
    
    static void moveLastStable(int[] a,int n,int key) {
		for(int i=0; i< n;i++) {
			if(a[i] == key)
				for(int j = i+1;j<n;j++) {
					if(a[j] != key) {
						int temp = a[i];
						a[i] = a[j];
						a[j] = temp;
						
						break;
					}
				}
		}
	}
    
    public void moveZeroes(int[] a) {
   
        moveLastStable(a,a.length,0);
    }
}
