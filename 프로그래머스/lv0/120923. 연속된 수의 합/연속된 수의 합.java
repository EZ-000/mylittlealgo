class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        for (int start = -50; start <= total; start++) {
            int sum = 0;
            for (int offset = 0; offset < num; offset++) sum += start + offset;
            if (sum == total) {
                for (int offset = 0; offset < num; offset++) answer[offset] = start + offset;
                break;
            }
        }
        return answer;
    }
}