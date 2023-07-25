class Solution {
    public int solution(int n) {
        String ternery = Integer.toString(n, 3);
        StringBuilder builder = new StringBuilder();
        builder.append(ternery).reverse();

        return Integer.parseInt(builder.toString(), 3);
    }
}