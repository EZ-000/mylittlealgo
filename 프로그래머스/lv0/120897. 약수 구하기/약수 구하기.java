import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int number = 1; number < n + 1; number++) {
            if (n % number == 0) answer.add(number);
        }
        return answer
            .stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}