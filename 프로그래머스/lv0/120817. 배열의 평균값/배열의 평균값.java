class Solution {
    public double solution(int[] numbers) {
        double length = numbers.length;
        double sumOfNums = 0;
        
        for (int number : numbers) {
            sumOfNums += number;
        }
        
        double answer = sumOfNums / length;
        return answer;
    }
}