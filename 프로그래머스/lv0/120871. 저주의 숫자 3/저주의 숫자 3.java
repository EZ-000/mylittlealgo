import java.util.Arrays;

class Solution {
    public int solution(int n) {
        int[] numbers = new int[n];
        int now = 1;
        for (int i = 0; i < n; i++) {
            while (true) {
                boolean condition1 = (now % 3 == 0);
                boolean condition2 = false;
                for (char c : String.valueOf(now).toCharArray()) {
                    if (c == '3') {
                        condition2 = true;
                    }
                }
                if (!condition1 & !condition2) break;
                now++;
            }
            numbers[i] = now;
            now++;
        }
        
        return numbers[n - 1];
    }
}