import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(String s) {
        String[] letters = s.split("");
        Arrays.sort(letters, Comparator.reverseOrder());
        return String.join("", letters);
    }
}