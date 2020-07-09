class Solution {
    	static int[] nextDay(int[] a) {
		int n = a.length;
		int[] res =  new int[n];
		
		for(int i=1;i<n-1;i++) 
			res[i] = ((a[i-1] ^ a[i+1]) ^ 1);
		
		return res;
	}
	
	static int[] fn(int[] cells,int N) {
		if(cells==null || cells.length==0 || N<=0) return cells;
        boolean hasCycle = false;
        int cycle = 0;
        HashSet<String> set = new HashSet<>(); 
        for(int i=0;i<N;i++){
            int[] next = nextDay(cells);
            String key = Arrays.toString(next);
            if(!set.contains(key)){ 
                set.add(key);
                cycle++;
            }
            else{
                hasCycle = true;
                break;
            }
            cells = next;
        }
        if(hasCycle){
            N = N%cycle;
            for(int i=0;i<N;i++){
                cells = nextDay(cells);
            }   
        }
       
        return cells;
		
	}
    
    public int[] prisonAfterNDays(int[] cells, int N) {
        return fn(cells,N);
    }
}
