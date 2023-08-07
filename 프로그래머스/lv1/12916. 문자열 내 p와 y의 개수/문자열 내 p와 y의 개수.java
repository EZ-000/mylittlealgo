class Solution {
    boolean solution(String s) {
        int cntP = 0;
        int cntY = 0;
        
        for (int index = 0; index < s.length(); index++) {
            if (s.charAt(index) == 'P' || s.charAt(index) == 'p') cntP += 1;
            else if (s.charAt(index) == 'Y' || s.charAt(index) == 'y') cntY += 1;
        }

        return (cntP == cntY) ? true : false;
    }
}