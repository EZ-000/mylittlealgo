import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int length = numbers.length;
        int result1 = numbers[length - 2] * numbers[length - 1];
        int result2 = numbers[0] * numbers[1];
        
        int answer = (result2 < result1) ? result1 : result2;
        return answer;
    }
}