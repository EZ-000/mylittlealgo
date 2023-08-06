import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(String[] babblings) {
        Map<String, String> dict = new HashMap<>(){{
            put("a","aya");
            put("y","ye");
            put("w","woo");
            put("m","ma");
        }};
        
        int answer = 0;
        for (String babbling : babblings) {
            int index = 0;
            boolean flag = true;
            while (flag) {
                if (babbling.length() <= index) break;
                String start = String.valueOf(babbling.charAt(index));
                String check = dict.getOrDefault(start, "none");
                if (check.equals("none")) flag = false;
                else {
                    int offset = check.length();
                    if (babbling.length() < index + offset) flag = false;
                    else if (!babbling.substring(index, index + offset).equals(check)) flag = false;
                    else index += offset;
                }
            }
            if (flag) answer += 1;
        }
        return answer;
    }
}