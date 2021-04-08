class Solution {
    public int removeDuplicates(int[] nums) {
       int tracker = 0,  begin = 0, end =0;
    
        while(end < nums.length){
            if(nums[begin] != nums[end]){
                nums[++tracker] = nums[end];
                begin = end;
            }
            end++;
        }

        return tracker+1;
        
    }
}