import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> counts = new HashMap<String, Integer>();

        for (String person : participant) {
            if (counts.containsKey(person)) counts.put(person, counts.get(person) + 1);
            else counts.put(person, 0);
        }

        for (String person : completion) {
            counts.put(person, counts.get(person) - 1);
        }

        String answer = "";
        for (String key : counts.keySet()) {
            if (counts.get(key) == 0) {
                answer = key;
                break;
            }
        }

        return answer;
    }
}