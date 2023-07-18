import java.util.HashMap;

class Solution {
    public String solution(String rsp) {
        HashMap<String, String> win = new HashMap<>(){{
            put("2","0");
            put("0","5");
            put("5","2");
        }};
        
        String[] rspArray = rsp.split("");
        String answer = "";
        for (String hand : rspArray) {
            answer += win.get(hand);
        }
        
        return answer;
    }
}