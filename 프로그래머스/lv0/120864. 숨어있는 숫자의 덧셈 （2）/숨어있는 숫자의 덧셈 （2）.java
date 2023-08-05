import java.util.Arrays;

class Solution {
    public int solution(String myString) {
        String[] numbers = myString.split("\\D+");
        
        int answer = 0;
        for (String number : numbers) {
            if (!number.equals("")) answer += Integer.valueOf(number);
        }
        return answer;
    }
}