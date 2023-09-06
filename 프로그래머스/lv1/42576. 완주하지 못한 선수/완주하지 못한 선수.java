import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        String answer = "";
        for (int index = 0; index < completion.length; index++) {
            if (!participant[index].equals(completion[index])) {
                answer = participant[index];
                break;
            }
        }
        if (answer.equals("")) answer = participant[participant.length - 1];
        
        return answer;
    }
}