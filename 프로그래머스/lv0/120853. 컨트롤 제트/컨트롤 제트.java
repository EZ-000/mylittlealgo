class Solution {
    public int solution(String s) {
        String[] items = s.split(" ");
        
        int answer = 0;
        int pre = 0;
        for (String item : items) {
            if (item.equals("Z")) {
                answer -= pre;
            } else {
                int number = Integer.parseInt(item);
                answer += number;
                pre = number;
            }
        }
        return answer;
    }
}