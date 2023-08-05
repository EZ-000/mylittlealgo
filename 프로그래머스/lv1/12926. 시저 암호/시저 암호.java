class Solution {
    public String solution(String s, int n) {
        String caesarCipher = "";
        for (int index = 0; index < s.length(); index++) {
            char nowChar = s.charAt(index);
            char newChar = (char) ((nowChar == ' ') ? ' ' : nowChar + n);
            if (64 < nowChar && nowChar < 91) {
                if (90 < newChar) {
                    newChar = (char) (newChar % 91 + 65);
                }
            } else if (96 < nowChar && nowChar < 123) {
                if (122 < newChar) {
                    newChar = (char) (newChar % 123 + 97);
                }
            }
            caesarCipher += newChar;
        }
        return caesarCipher;
    }
}