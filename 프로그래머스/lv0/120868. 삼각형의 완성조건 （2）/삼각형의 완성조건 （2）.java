class Solution {
    public int solution(int[] sides) {
        int nowMax = (sides[1] < sides[0]) ? sides[0] : sides[1];
        int nowMin = (sides[1] < sides[0]) ? sides[1] : sides[0];
        return 2 * nowMin - 1;
    }
}