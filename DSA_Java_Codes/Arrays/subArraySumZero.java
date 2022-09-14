class Solution {
    
    static int maxSubZero(int[] a,int n) {
		int maxL = 0;
		int curSum = 0;
		
		HashMap<Integer,Integer> map = new HashMap<>();
		
		for(int i=0;i<n;i++) {
			curSum += a[i];
			
			if(curSum == 0)
				maxL = Math.max(maxL, i+1);
			else if (map.containsKey(curSum))
				maxL = Math.max(maxL, i - map.get(curSum));
			else
				map.put(curSum,i);
		}
		
		
		return maxL;
	}
    
    public int findMaxLength(int[] nums) {
        int n = nums.length;
        for(int i=0;i<n;i++) nums[i] = (nums[i]==0) ? -1 : 1;
        
        return maxSubZero(nums,n);
    }
}
