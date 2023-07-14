class Solution {
    public String solution(String myString, String letter) {
        int letterNum = (int) letter.charAt(0);
        
        String answer = "";
        for (int i = 0; i < myString.length(); i++) {
            if ((int) myString.charAt(i) != letterNum) {
                answer += myString.charAt(i);
            }
        }
        
        return answer;
    }
}