class Solution {
    
    public void solveSudoku(char[][] board) {
        backtracking(board);
    }
    
    public boolean backtracking(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                
                // 보드에 숫자가 있다면 continue
                if (board[i][j] != '.') continue;
                
                // 각 빈칸마다 arraylist를 만들고, 어떤 숫자가 들어갈 수 있는지 확인한다. 
                ArrayList<Character> arr = validValues(board, i, j);
                
                // 각각의 value를 넣고 가능한지 확인한다. 
                for (char x : arr) {
                    board[i][j] = x;
                    
                    // true => solved
                    if (backtracking(board)) return true;
                    // 그렇지 않다면 backtracking 진행 
                    else board[i][j] = '.';
                }
                return false;
            }
        } 
        return true;
    }
    
    // 가능한 value 값들의 arraylist를 리턴한다.
    public ArrayList<Character> validValues(char[][] board, int a, int b) {
        
        // 가능한 값들 선언
        ArrayList<Character> arr = new ArrayList<Character>(Arrays.asList('1', '2', '3', '4', '5', '6', '7', '8', '9'));
        
        // 현재 채우고자 하는 칸
        char target = board[a][b];
        
        // 가로와 세로줄에 있는 값들을 다 제거한다. 
        for (int i = 0; i < 9; i++) {
            arr.remove(Character.valueOf(board[a][i]));
            arr.remove(Character.valueOf(board[i][b]));
        }
        
        // 박스 값을 고려하며 박스 값 제거한다. 
        int boxrow = (a / 3) * 3, boxcol = (b / 3) * 3;
        
        for (int i = boxrow; i < boxrow+3; i++) {
           for (int j = boxcol; j < boxcol+3; j++) {
                arr.remove(Character.valueOf(board[i][j]));
            } 
        }
        
        return arr;
    }
}