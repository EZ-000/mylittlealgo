import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] numlist) {
        ArrayList<Integer> multiples = new ArrayList<>();
        
        for (int num : numlist) {
            if (num % n == 0) multiples.add(num);
        }
        
        return multiples.stream().mapToInt(Integer::intValue).toArray();
    }
}