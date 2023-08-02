import java.util.HashMap;

class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        HashMap<String, int[]> direction = new HashMap<>() {{
            put("up",new int[] {0, 1});
            put("down",new int[] {0, -1});
            put("left",new int[] {-1, 0});
            put("right",new int[] {1, 0});
        }};
        
        int[] answer = {0, 0};
        int width = board[0] / 2;
        int height = board[1] / 2;
        for (String input : keyinput) {
            int nr = answer[0] + direction.get(input)[0];
            int nc = answer[1] + direction.get(input)[1];
            if ((-width <= nr & nr <= width) & (-height <= nc & nc <= height)) {
                answer[0] = nr;
                answer[1] = nc;
            }
        }
        
        return answer;
    }
}