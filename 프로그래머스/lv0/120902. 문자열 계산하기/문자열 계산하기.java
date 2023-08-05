import java.util.Arrays;

class Solution {
    public int solution(String myString) {
        String[] items = myString.split(" ");
        
        int answer = Integer.parseInt(items[0]);
        for (int index = 1; index < items.length; index += 2) {
            String op = items[index];
            switch (op) {
                case "+":
                    answer += Integer.parseInt(items[index + 1]);
                    break;
                case "-":
                    answer -= Integer.parseInt(items[index + 1]);
                    break;
            }
        }
        return answer;
    }
}