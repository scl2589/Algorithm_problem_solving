class Solution {
    public boolean isValid(String s) {
        ArrayList arr = new ArrayList();
        
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (current == '(' || current == '{' || current == '[') {
                arr.add(current); 
            }
            else {
                if (arr.size() < 1) {
                    return false;
                } else {
                    char last = (char)arr.get(arr.size()-1);
                    arr.remove(arr.size()-1); 
                    if (current == '}' && last == '{') continue;
                    else if (current == ']' && last == '[') continue;
                    else if (current==')' && last == '(') continue;
                    else {
                        return false; 
                    }
                }
            }
        }
        if (arr.size() >= 1) {
            return false;
        }
        return true;
    }
}