class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String target = String.valueOf(k);
        for (int number = i; number < j + 1; number++) {
            String original = String.valueOf(number);
            String replaced = original.replace(target, "");
            answer += original.length() - replaced.length();
        }
        return answer;
    }
}