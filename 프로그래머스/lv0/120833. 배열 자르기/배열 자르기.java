class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int length = num2 - num1 + 1;
        int[] answer = new int[length];
        for (int n = 0; n < length; n++) {
            answer[n] = numbers[n + num1];
        }
        return answer;
    }
}