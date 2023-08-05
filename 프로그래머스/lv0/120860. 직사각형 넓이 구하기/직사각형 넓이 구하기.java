class Solution {
    public int solution(int[][] dots) {
        int width = 0;
        int height = 0;
        
        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                width = (width == 0)
                    ? dots[i][0] - dots[j][0]
                    : width;
                height = (height == 0)
                    ? dots[i][1] - dots[j][1]
                    : height;
                if (width != 0 && height != 0) break;
            }
        }
        
        int answer = (0 < width * height) ? width * height : -1 * width * height;
        return answer;
    }
}