class Solution {
    public int[] solution(int[] numList) {
        int len = numList.length;
        int[] answer = new int[len];
        
        for (int i = 0; i < len; i++) {
            answer[i] = numList[len - i - 1];
        }
        
        return answer;
    }
}