import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int length = numbers.length;
        return numbers[length - 2] * numbers[length - 1];
    }
}