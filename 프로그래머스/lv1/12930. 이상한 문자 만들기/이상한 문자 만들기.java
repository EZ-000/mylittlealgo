class Solution {
    public String solution(String s) {
        String answer = "";
        int index = 0;
        String[] chars = s.split("");
        
        for (String c : chars) {
            index = c.equals(" ") ? 0 : index + 1;
            answer += (index % 2 == 0) ? c.toLowerCase() : c.toUpperCase();
        }
        
        return answer;
    }
}