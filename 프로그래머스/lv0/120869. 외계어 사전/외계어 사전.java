class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;
        for (String word : dic) {
            String test = word;
            for (String c : spell) test = test.replaceFirst(c, "");
            if (test.length() == 0 & word.length() == spell.length) {
                answer = 1;
                break;
            }
        }
        return answer;
    }
}