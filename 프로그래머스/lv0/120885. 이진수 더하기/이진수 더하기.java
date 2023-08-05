class Solution {
    public String solution(String bin1, String bin2) {
        int result = Integer.valueOf(bin1, 2) + Integer.valueOf(bin2, 2);
        return Integer.toString(result, 2);
    }
}