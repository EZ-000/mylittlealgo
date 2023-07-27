class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int diff = 100;
        for (int number : array) {
            int nowDiff = (n - number < 0) ? number - n : n - number;
            if (nowDiff <= diff) {
                if (nowDiff == diff & answer < number) continue;
                diff = nowDiff;
                answer = number;
            }
        }
        return answer;
    }
}