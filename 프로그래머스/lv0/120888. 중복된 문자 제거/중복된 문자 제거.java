class Solution {
    public String solution(String myString) {
        StringBuilder builder = new StringBuilder();
        boolean[] visited = new boolean[127];
        
        for (char c : myString.toCharArray()) {
            if (!visited[c]) {
                visited[c] = true;
                builder.append(c);
            }
        }
        return builder.toString();
    }
}