class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        for (int index = 0; index < cipher.length(); index++) {
            if ((index + 1) % code == 0) answer += cipher.charAt(index);
        } 
        return answer;
    }
}