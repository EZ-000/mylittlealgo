import java.lang.Math;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] solution(int n) {
        Set<Integer> primeNumbers = new HashSet<Integer>();
        for (int primeNumber = 2; primeNumber <= n; primeNumber++) {
            while (n % primeNumber == 0) {
                n /= primeNumber;
                primeNumbers.add(primeNumber);
            }
        }
        
        int[] answer = Arrays
            .stream(primeNumbers.toArray(new Integer[0]))
            .mapToInt(Integer::intValue)
            .toArray();
        
        Arrays.sort(answer);
        
        return answer;
    }
}