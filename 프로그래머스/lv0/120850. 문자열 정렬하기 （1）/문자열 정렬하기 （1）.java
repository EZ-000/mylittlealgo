import java.util.Arrays;

class Solution {
    public int[] solution(String myString) {
        char[] chars = myString.toCharArray();
        String numbers = "";
        for (char c : chars) {
            int asciiNum = c - '0';
            if (0 <= asciiNum && asciiNum < 10) {
                numbers += asciiNum;
            }
        }
        
        int[] answer = new int[numbers.length()];
        for (int i = 0; i < numbers.length(); i++) {
            answer[i] = numbers.charAt(i) - '0';
        }
        Arrays.sort(answer);
        return answer;
    }
}