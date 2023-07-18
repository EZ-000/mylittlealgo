import java.util.HashMap;

class Solution {
    public String solution(int age) {
        HashMap<String, String> dict = new HashMap<>(){{
            put("0","a");
            put("1","b");
            put("2","c");
            put("3","d");
            put("4","e");
            put("5","f");
            put("6","g");
            put("7","h");
            put("8","i");
            put("9","j");
        }};
        
        String strAge = age + "";
        String answer = "";
        for (int i = 0; i < strAge.length(); i++) {
            String keyNum = strAge.charAt(i) + "";
            answer += dict.get(keyNum);
        }
        return answer;
    }
}