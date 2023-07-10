class Solution {
    public int solution(int[] array) {
        int[] visited = new int[1001];
        
        for (int i = 0; i < array.length; i++) {
            visited[array[i]] += 1;
        }
        
        boolean flag = false;
        int maxNum = 0;
        int answer = -1;
        for (int i = 0; i < 1001; i++) {
            if (maxNum == visited[i]) {
                flag = true;
            }
            if (maxNum < visited[i]) {
                flag = false;
                maxNum = visited[i];
                answer = i;
            }
        }
        
        answer = (flag) ? -1 : answer;
        return answer;
    }
}