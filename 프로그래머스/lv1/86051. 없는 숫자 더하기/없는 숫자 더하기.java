class Solution {
    public int solution(int[] numbers) {
        boolean[] visited = {false, false, false, false, false, false, false, false, false, false};
        for (int number : numbers) {
            visited[number] = true;
        }

        int answer = 0;
        for (int n = 0; n < 10; n++) {
            if (!visited[n]) answer += n;
        }
        
        return answer;
    }
}