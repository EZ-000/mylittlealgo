class Solution {
    public String solution(String myString, int n) {
        String answer = "";
        
        for (int i = 0; i < myString.length(); i++) {
            answer += Character.toString(myString.charAt(i)).repeat(n);
        }
        
        return answer;
    }
}