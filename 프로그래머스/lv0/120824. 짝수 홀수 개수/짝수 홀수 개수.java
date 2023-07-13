class Solution {
    public int[] solution(int[] numList) {
        int[] answer = {0, 0};
        
        for (int i = 0; i < numList.length; i++) {
            if (numList[i] % 2 == 0) {
                answer[0] += 1;
            } else {
                answer[1] += 1;
            }
        }
        
        return answer;
    }
}