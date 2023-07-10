class Solution {
    public int solution(int[] array) {
        int[] visited = new int[1001];
        
        for (int i = 0; i < array.length; i++) {
            visited[array[i]] += 1;
        }
        
        boolean flag = false;
        int max_num = 0;
        int answer = -1;
        for (int i = 0; i < 1001; i++) {
            if (max_num == visited[i]) {
                flag = true;
            }
            if (max_num < visited[i]) {
                flag = false;
                max_num = visited[i];
                answer = i;
            }
        }
        
        answer = (flag) ? -1 : answer;
        return answer;
    }
}