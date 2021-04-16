class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        String[] arr = s.split(" ");
        String lastWord = arr[arr.length-1];
        System.out.println(lastWord);
        return lastWord.length();
        
    }
}