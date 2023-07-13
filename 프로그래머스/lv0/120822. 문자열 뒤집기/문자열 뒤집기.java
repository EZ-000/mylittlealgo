class Solution {
    public String solution(String myString) {
        String answer = "";
        
        int len = myString.length();
        for (int i = 0; i < len; i++) {
            answer += myString.charAt(len - i - 1);
        }
        
        return answer;
    }
}