class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for (int number : array) {
            String strNum = String.valueOf(number);
            for (char c : strNum.toCharArray()) {
                if (c == '7') answer += 1;
            }
        }
        return answer;
    }
}