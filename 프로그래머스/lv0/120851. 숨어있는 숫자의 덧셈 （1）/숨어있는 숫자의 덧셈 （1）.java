class Solution {
    public int solution(String myString) {
        myString = myString.replaceAll("[a-zA-Z]", "");
        
        int answer = 0;
        for (int i = 0; i < myString.length(); i++) {
            answer += myString.charAt(i) - '0';
        }
        
        return answer;
    }
}