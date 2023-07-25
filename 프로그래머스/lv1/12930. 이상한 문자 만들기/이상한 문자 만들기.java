class Solution {
    public String solution(String s) {
        StringBuilder builder = new StringBuilder();
        boolean flag = true;
        for (int i = 0; i < s.length(); i++) {
            String nowChar = String.valueOf(s.charAt(i));
            if (nowChar.equals(" ")) {
                builder.append(nowChar);
                flag = true;
            } else if (flag) {
                builder.append(nowChar.toUpperCase());
                flag = false;
            } else {
                builder.append(nowChar.toLowerCase());
                flag = true;
            }
        }
        return builder.toString();
    }
}