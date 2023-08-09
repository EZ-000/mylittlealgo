import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] way1 = {1, 2, 3, 4, 5};
        int[] way2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] way3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] scores = new int[3];
        for (int index = 0; index < answers.length; index++) {
            if (answers[index] == way1[index % way1.length]) scores[0] += 1;
            if (answers[index] == way2[index % way2.length]) scores[1] += 1;
            if (answers[index] == way3[index % way3.length]) scores[2] += 1;
        }
        
        int max = -1;
        for (int score : scores) {
            if (max < score) max = score;
        }
        
        List<Integer> answer = new ArrayList<>();
        for (int index = 0; index < 3; index++) {
            if (scores[index] == max) answer.add(index + 1);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}