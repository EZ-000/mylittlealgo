class Solution {
    public int[] solution(int[] numbers, String direction) {
        int length = numbers.length;
        int[] answer = new int[length];
        int index = 0;
        if (direction.equals("right")){
            answer[0] = numbers[length - 1];
            for (int i = 0; i < length - 1; i++) {
                answer[i + 1] = numbers[i];
            }
        } else {
            answer[length - 1] = numbers[0];
            for (int i = 0; i < length - 1; i++) {
                answer[i] = numbers[i + 1];
            }
        }
        return answer;
    }
}