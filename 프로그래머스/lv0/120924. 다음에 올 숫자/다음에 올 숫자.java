class Solution {
    public int solution(int[] common) {
        int cd1 = common[1] - common[0];
        int cd2 = common[2] - common[1];
        int cr = (common[0] != 0) ? common[1] / common[0] : 0;
        int lastTerm = common[common.length - 1];
        
        int answer = 0;
        if (cd1 == cd2) answer = lastTerm + cd1;
        else answer = lastTerm * cr;
        
        return answer;
    }
}