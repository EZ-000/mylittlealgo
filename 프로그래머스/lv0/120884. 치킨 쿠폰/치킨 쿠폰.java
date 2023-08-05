class Solution {
    public int solution(int chicken) {
        return (chicken < 10) ? 0 : (chicken - 10) / 9 + 1;
    }
}