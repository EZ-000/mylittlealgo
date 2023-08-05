class Solution {
    public int[] solution(String s) {
        int changeCnt = 0;
        int zeroCnt = 0;
        while (!s.equals("1")) {
            changeCnt += 1;

            String newS = s.replace("0", "");
            zeroCnt += s.length() - newS.length();
            
            s = Integer.toString(newS.length(), 2);
        }

        return new int[] {changeCnt, zeroCnt};
    }
}