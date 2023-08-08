class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int plus = (brown + 4) / 2;
        int multi = brown + yellow;
        
        for (int w = 3; w < multi; w++) {
            int h = multi / w;
            if (multi % w == 0 & w == plus - h) {
                answer[0] = (h < w) ? w : h;
                answer[1] = (h < w) ? h : w;
            } 
        }
        return answer;
    }
}