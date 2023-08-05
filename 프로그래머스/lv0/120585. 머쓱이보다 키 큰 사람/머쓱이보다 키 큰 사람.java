class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for (int friend : array) {
            if (height < friend) answer++;
        }
        return answer;
    }
}