class Solution {
    public boolean isPalindrome(int x) {
        // int를 String으로 변환한다. 
        String xStr = String.valueOf(x); 
        
        for (int i = 0; i < xStr.length()/2; i++) {
            if (xStr.charAt(i) != xStr.charAt(xStr.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}