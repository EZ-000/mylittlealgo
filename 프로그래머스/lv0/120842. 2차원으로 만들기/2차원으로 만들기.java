class Solution {
    public int[][] solution(int[] numbers, int n) {
        int[][] answer = new int[numbers.length / n][n];
        
        int index = 0;
        for (int i = 0; i < numbers.length; i += n) {
            for (int j = 0; j < n; j++) {
                answer[index][j] = numbers[i + j];
            }
            index++;
        }
        
        return answer;
    }
}