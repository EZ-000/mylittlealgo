import java.util.Arrays;

class Solution {
    public String solution(String myString) {
        char[] chars = myString.toLowerCase().toCharArray();
        Arrays.sort(chars);
        return String.valueOf(chars);
    }
}