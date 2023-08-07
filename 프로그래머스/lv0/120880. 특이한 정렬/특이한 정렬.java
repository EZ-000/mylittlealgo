import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        int max = 0;
        Set<Integer> diffs = new HashSet<Integer>();
        for (int index = 0; index < numlist.length; index++) {
            int diff = numlist[index] - n;
            diffs.add(diff);
            max = (max < Math.abs(diff)) ? Math.abs(diff) : max;
        }
        
        int[] answer = new int[numlist.length];
        int index = 0;
        for (int offset = 0; offset < max + 1; offset++) {
            if (diffs.contains(offset)) {
                answer[index] = n + offset;
                index++;
                if (offset == 0) continue;
            }
            if (diffs.contains(-offset)) {
                answer[index] = n - offset;
                index++;
            }
        }
        
        
        return answer;
    }
}