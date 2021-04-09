class Solution {
    public int removeElement(int[] nums, int val) {
        int[] arr;
        arr = new int[nums.length];
        int res = 0;
        
        for(int i=0;i<nums.length;i++){
            if(val!=nums[i]){
                arr[res]=nums[i];
                res++;
            }
        }
        for(int i=0;i<res;i++){
            nums[i]=arr[i];
        }
        return res;
    }
}