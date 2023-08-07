class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        if (!(s.length() == 4 || s.length() == 6) || !s.matches("[0-9]*")) answer = false;
        return answer;
    }
}