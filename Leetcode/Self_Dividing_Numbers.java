/**

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

*/

class Solution {
    
    static boolean checkSelf(int n){
        int num = n;
        int rem;
        
        while(n != 0){
            rem = n % 10;
            
            if(rem == 0 || num % rem != 0) return false;
            
            n = n/10;
        }
        
        return true;
    }
    
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<>();
        
        for(int i=left;i<=right;i++)
            if(checkSelf(i))
                res.add(i);
        
        return res;
    }
}
