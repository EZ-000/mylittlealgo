class Solution {
    public int solution(String A, String B) {
        int answer = -1;
        int len = A.length();
        for (int offset = 0; offset < len; offset++) {
            char[] pushed = new char[len];
            for (int index = 0; index < len; index++) {
                pushed[(index + offset) % len] = A.charAt(index);
            }
            String newA = new String(pushed);
            if (B.equals(newA)) {
                answer = offset;
                break;
            }
        }
        
        return answer;
    }
}