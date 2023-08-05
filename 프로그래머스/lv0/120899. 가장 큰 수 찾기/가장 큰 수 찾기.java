class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[] {0, 0};
        
        for (int index = 0; index < array.length; index++) {
            if (answer[0] < array[index]) {
                answer[0] = array[index];
                answer[1] = index;
            }
        }
        
        return answer;
    }
}