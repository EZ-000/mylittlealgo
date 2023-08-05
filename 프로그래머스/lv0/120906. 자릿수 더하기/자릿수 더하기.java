class Solution {
    public int solution(int n) {
        String[] numbers = String.valueOf(n).split("");
        
        int answer = 0;
        for (String number : numbers) answer += Integer.parseInt(number);
        return answer;
    }
}