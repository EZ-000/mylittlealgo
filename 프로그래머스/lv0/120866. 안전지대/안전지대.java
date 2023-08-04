class Solution {
    public int solution(int[][] board) {
        int rowLen = board.length;
        int colLen = board[0].length;
        int[][] neighbors = {
            {0, 0},
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1},
            {-1, -1},
            {1, 1},
            {-1, 1},
            {1, -1},
        };
        
        int[][] danger = new int[rowLen][colLen];
        int answer = rowLen * colLen;
        for (int row = 0; row < rowLen; row++) {
            for (int col = 0; col < colLen; col++) {
                if (board[row][col] == 1) {
                    for (int[] neighbor : neighbors) {
                        int nr = row + neighbor[0];
                        int nc = col + neighbor[1];
                        if (-1 < nr & nr < rowLen & -1 < nc & nc < colLen) {
                            if (danger[nr][nc] != 1) {
                                answer -= 1;
                                danger[nr][nc] = 1;
                            }
                        }
                    }
                }
            }
        }
        return answer;
    }
}