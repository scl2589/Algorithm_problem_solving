class Solution {
    public int strStr(String haystack, String needle) {
        int M = needle.length();
        int N = haystack.length();
        if (N == 0 && M == 0) {
            return 0;
        } else if (N ==0 && M > 0) {
            return -1;
        } else {
            int i = 0;
            while(i <= N - M) {
                int j = 0;
                while(j < M) {
                    if(haystack.charAt(i + j) != needle.charAt(j)) break;
                    j++;
                }
                if(j == M) return i;
                i++;
            }
            return -1;
        }
    }
}