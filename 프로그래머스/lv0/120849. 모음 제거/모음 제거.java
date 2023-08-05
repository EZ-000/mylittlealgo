class Solution {
    public String solution(String myString) {
        char[] chars = myString.toCharArray();
        String answer = "";
        for (char c : chars) {
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                answer += c;
            }
        }
        return answer;
    }
}