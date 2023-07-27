import java.util.HashMap;

class Solution {
    public long solution(String numbers) {
        HashMap<String, String> dict = new HashMap<>(){{
            put("zero","0");
            put("one","1");
            put("two","2");
            put("three","3");
            put("four","4");
            put("five","5");
            put("six","6");
            put("seven","7");
            put("eight","8");
            put("nine","9");
        }};
        
        StringBuilder answer = new StringBuilder();
        StringBuilder number = new StringBuilder();
        for (int index = 0; index < numbers.length(); index++) {
            number.append(numbers.charAt(index));
            String key = number.toString();
            if (dict.containsKey(key)) {
                answer.append(dict.get(key));
                number = new StringBuilder();
            }
        }
        return Long.valueOf(answer.toString());
    }
}