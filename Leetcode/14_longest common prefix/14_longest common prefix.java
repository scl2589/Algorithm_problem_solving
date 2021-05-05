class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int leastLength = 201;
        for (int i = 0; i < strs.length; i ++) {
            if (strs[i].length() < leastLength) {
                leastLength = strs[i].length();
            }
        }
        String answer = "";
        char temp; 
        Boolean flag = true ;
        for (int i = 0; i < leastLength; i++) {
            temp = strs[0].charAt(i); 
            for (int j= 0; j < strs.length; j++) {
                if (strs[j].charAt(i) != temp) {
                    flag = false; 
                    break;
                }
            }
            if (flag) {
                answer += temp; 
            } else {
                break;
            }
        }
        return answer;
    }
}