class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        int str1len = str1.length();
        int str2len = str2.length();

        for (int index = 0; index < str1len; index++) {
            if (str1.charAt(index) == str2.charAt(0) && index + str2len <= str1len) {
                String substr = str1.substring(index, index + str2len);
                if (substr.equals(str2)) {
                    answer = 1;
                    break;
                }
            }
        }
        
        return answer;
    }
}