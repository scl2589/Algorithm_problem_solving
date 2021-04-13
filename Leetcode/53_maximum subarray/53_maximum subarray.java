// 시간초과 코드
class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int max_sum = -1000000;
        for (int len = 1; len <= nums.length; len++) {
            for (int i = 0; i < nums.length - len + 1; i++) {
                int sum = 0;
                for (int j = i; j < i + len; j++) {
                    sum += nums[j];
                }
                if (max_sum < sum) {
                    max_sum = sum;
                }
            
            }
        }
        return max_sum;
    }
}