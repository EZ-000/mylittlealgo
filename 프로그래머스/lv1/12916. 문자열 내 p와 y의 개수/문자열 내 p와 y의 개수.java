class Solution {
    boolean solution(String s) {
        int count = 0;
        
        for (int index = 0; index < s.length(); index++) {
            if (s.charAt(index) == 'P' || s.charAt(index) == 'p') count += 1;
            else if (s.charAt(index) == 'Y' || s.charAt(index) == 'y') count -= 1;
        }

        return (count == 0) ? true : false;
    }
}