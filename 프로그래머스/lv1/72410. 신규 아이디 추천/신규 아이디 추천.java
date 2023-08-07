class Solution {
    public String solution(String new_id) {
        // 1단계
        new_id = new_id.toLowerCase();
        // 2단계
        new_id = new_id.replaceAll("[^a-z0-9\\-_.]","");
        // 3단계
        new_id = new_id.replaceAll("\\.{2,}",".");
        // 4단계
        new_id = new_id.replaceAll("^\\.|\\.$","");
        // 5단계
        new_id = (new_id.isEmpty()) ? "a" : new_id;
        // 6단계
        new_id = (16 <= new_id.length()) ? new_id.substring(0, 15) : new_id;
        new_id = new_id.replaceAll("\\.$","");
        // 7단계
        int length = new_id.length();
        String last = String.valueOf(new_id.charAt(length - 1));
        new_id = (length < 3) ? new_id + last.repeat(3 - length) : new_id;
        return new_id;
    }
}