class Solution {
    public String[] solution(String myStr, int n) {
        int myStrLen = myStr.length();
        int length = (myStrLen % n == 0) ? myStrLen / n : myStrLen / n + 1;
        String[] answer = new String[length];
        for (int index = 0; index < length; index++) {
            int start = index * n;
            int end = (start + n <= myStrLen) ? start + n : myStrLen;
            answer[index] = myStr.substring(start, end);
        }
        return answer;
    }
}