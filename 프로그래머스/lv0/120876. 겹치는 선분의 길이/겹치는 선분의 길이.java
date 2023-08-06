import java.util.Arrays;

class Solution {
    private int findStart(int[][] lines) {
        int start = 101;
        for (int index = 0; index < lines.length; index++) {
            if (lines[index][0] < start) start = lines[index][0];
        }
        return start;
    }
    
    private int findEnd(int[][] lines) {
        int end = -101;
        for (int index = 0; index < lines.length; index++) {
            if (end < lines[index][1]) end = lines[index][1];
        }
        return end;
    }
    
    private void checkOverlapped(int s1, int e1, int s2, int e2, int offset, int[] visited) {
        int middle = 0;
        int middleEnd = 0;
        if (s2 <= s1 & s1 <= e2) {
            middle = s1;
            middleEnd = (e1 < e2) ? e1 : e2;
        } else if (s1 <= s2 & s2 <= e1) {
            middle = s2;
            middleEnd = (e1 < e2) ? e1 : e2;
        }
        for (int m = middle; m < middleEnd; m++) visited[m + offset] = 1;
    }
    
    public int solution(int[][] lines) {
        int start = findStart(lines);
        int end = findEnd(lines);
        
        int[] visited = new int[end - start];
        for (int i = 0; i < 3; i++) {
            for (int j = i + 1; j < 3; j++) {
                checkOverlapped(lines[i][0], lines[i][1], lines[j][0], lines[j][1], -start, visited);
            }
        }
        
        return Arrays.stream(visited).sum();
    }
}