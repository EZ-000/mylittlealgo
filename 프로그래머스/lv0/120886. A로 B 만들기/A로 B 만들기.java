import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int solution(String before, String after) {
        int length = before.length();
        int[] asciiForBefore = new int[128];
        int[] asciiForAfter = new int[128];
        
        for (int i = 0; i < length; i++) {
            asciiForBefore[before.charAt(i)] += 1;
            asciiForAfter[after.charAt(i)] += 1;
        }
        
        int answer = 1;
        for (int i = 0; i < 128; i++) {
            if (asciiForBefore[i] != asciiForAfter[i]) {
                answer = 0;
                break;
            } 
        }
        
        return answer;
    }
}