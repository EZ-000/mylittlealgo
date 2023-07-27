class Solution {
    public int[] solution(String[] strlist) {
        int length = strlist.length;
        int[] answer = new int[length];
        
        for (int i = 0; i < length; i++) {
            answer[i] = strlist[i].length();
        }
        return answer;
    }
}