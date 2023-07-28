class Solution {
    public int solution(int num, int k) {
        String number = String.valueOf(num);
        
        int answer = -1;
        for (int index = number.length() - 1; -1 < index; index--) {
            int nowNum = Integer.parseInt(number.substring(index, index + 1));
            if (nowNum == k) answer = index + 1;
        }
        return answer;
    }
}