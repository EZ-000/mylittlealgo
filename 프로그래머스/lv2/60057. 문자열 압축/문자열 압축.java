class Solution {
    private int getCompressedLength(String s, int u) {
        StringBuilder builder = new StringBuilder();
        String now = s.substring(0, u);
        int cnt = 1;
        for (int index = u; index < s.length() + 1; index += u) {
            int end = (s.length() <= index + u) ? s.length() : index + u;
            String next = s.substring(index, end);
            if (now.equals(next)) {
                cnt += 1;
            } else {
                if (cnt == 1) {
                    builder.append(now);
                } else {
                    builder.append(cnt + "" + now);
                }
                cnt = 1;
            }
            now = next;
        }
        builder.append(now);
        return builder.length();
    }
    
    public int solution(String s) {
        int answer = 1001;
        for (int unit = 1; unit <= s.length(); unit++) {
            int compressedLength = getCompressedLength(s, unit);
            if (compressedLength < answer) {
                answer = compressedLength;
            }
        }
        return answer;
    }
}