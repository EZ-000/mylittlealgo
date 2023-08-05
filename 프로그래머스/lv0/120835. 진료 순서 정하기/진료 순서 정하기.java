import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int length = emergency.length;
        int[] sortedEmergency = Arrays.copyOf(emergency, length);
        Arrays.sort(sortedEmergency);
        
        int[] answer = new int[length];
        for (int i = 0; i < length; i++) {
            int now = sortedEmergency[length - i - 1];
            for (int j = 0; j < length; j++) {
                if (emergency[j] == now) {
                    answer[j] = i + 1;
                    break;
                }
            }
        }
        
        return answer;
    }
}