class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int index = 0;
        for (String formula : quiz) {
            String[] items = formula.split(" ");
            int num1 = Integer.parseInt(items[0]);
            int num2 = Integer.parseInt(items[2]);
            int num3 = Integer.parseInt(items[4]);
            String op = items[1];
            int correct = 0;
            switch (op) {
                case "+":
                    correct = num1 + num2;
                    break;
                case "-":
                    correct = num1 - num2;
                    break;
            }
            if (correct == num3) answer[index] = "O";
            else answer[index] = "X";
            index++;
        }
        return answer;
    }
}