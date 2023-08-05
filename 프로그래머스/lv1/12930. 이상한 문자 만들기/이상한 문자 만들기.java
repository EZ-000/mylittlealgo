class Solution {
    public String solution(String s) {
        char[] chars = s.toCharArray();
        int index = 0;

        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ' ') index = 0;
            else chars[i] = (index++ % 2 == 0)
                    ? Character.toUpperCase(chars[i])
                    : Character.toLowerCase(chars[i]);
        }
        return String.valueOf(chars);
    }
}