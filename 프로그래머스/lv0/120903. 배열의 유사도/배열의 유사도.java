import java.util.HashMap;

class Solution {
    public int solution(String[] s1, String[] s2) {
        HashMap<String, Boolean> visited = new HashMap<>();
        
        for (String item : s1) visited.put(item, true);
        
        int answer = 0;
        for (String item : s2) {
            if (visited.containsKey(item)) answer += 1;
        }
        
        return answer;
    }
}