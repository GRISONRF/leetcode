class Solution {
    public int findPeakElement(int[] nums) {

        //binary seach approach
        //[1,2,4,2,1]
        
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            //get the middle element
            int m = left + (right - left) / 2;
            //we know a number is a peak if it's greater than the number in its right 
            if (nums[m] > nums[m+1]){
                // right = m
                right = m;
                
            } else if(nums[m] < nums[m+1]){//if m < m+ 1
                //left = m+1
                left = m + 1;
            } 

        }
        return left;


    }
}