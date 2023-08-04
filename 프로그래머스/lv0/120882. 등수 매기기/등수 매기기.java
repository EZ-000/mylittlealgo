import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        int len = score.length;
        Integer[] sums = new Integer[len];
        for (int index = 0; index < len; index++) {
            sums[index] = score[index][0] + score[index][1];
        }
        Arrays.sort(sums, Collections.reverseOrder());
        
        int[] answer = new int[len];
        for (int index = 0; index < len; index++) {
            int nowSum = score[index][0] + score[index][1];
            answer[index] = Arrays.asList(sums).indexOf(nowSum) + 1;
        }
        return answer;
    }
}