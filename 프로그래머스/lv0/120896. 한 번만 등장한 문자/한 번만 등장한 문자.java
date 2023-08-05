import java.util.Arrays;

class Solution {
    public String solution(String s) {
        boolean[] visited = new boolean[127];
        String sCopy = s;
        
        for (char c : s.toCharArray()) {
            if (visited[c]) sCopy = sCopy.replace(Character.toString(c), "");
            else visited[c] = true;
        }
        
        char[] answer = sCopy.toCharArray();
        Arrays.sort(answer);
        
        return String.valueOf(answer);
    }
}